---
title: The Google File System
updated: 2026-03-11 03:54:23Z
date: 2025-10-06 16:08:37Z
tags:
  - distributed
share: true
---

**Source**: [Paper by Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung Google](https://drive.google.com/file/d/1gWF-JCvqmaQrJcDQBe6CSqpJnep1q96a/view?usp=sharing)

Google File System (GFS) is a distributed file system developed at google. Other than conventional goals of any distributed system : performance, scalability, reliability & availability, its design was driven chiefly by key observations of existing workloads and usage patterns at google. 

## Assumptions
- It is build mostly for commodity hardware, were failure is norm rather than exception. With hundreds of machines and thousands of disks, disk failure and data corruption happens on a daily basis. System should be tolerant towards such failures. 
- Bigger multi GB files are more common than smaller ones.
- Files are written mostly in append only fashion. Random writes are rare. Small random writes are supported by system, but it doesn't have to be efficient.
- Files are read in large streaming in order rather than small random reads. 
- For performance, we need to allow multiple clients concurrently appending to the same file.
- Overall data bandwidth is more important than latency. Processing data in bulk at high rate is more important than response time for each write. 
- Since all clients of GFS are internal to google, design was heavily biased by internal infrastructure and based on the assumption that client libraries could be developed in sync with FS APIs.  

## Interface

GFS doesn't implement standard POSIX API for file system. Although it provides a familiar interface, files are organized hierarchically in directories. Standard operations allowed on the files are: create, delete, open, close, read, write & record append. Record append allows multiple concurrent clients to append data atomically to same file, that is, either the write is completely written in the file or not. Low cost snapshotting of a file or directory is supported. 

## Architecture

GFS mainly consists of three components: single master, multiple chunkservers and multiple clients. 

Files are divided into uniform sized chunks of 64 MB size, identified by immutable chunk handle. Master stores metadata, namely, files in namespace, mapping of files to chunks, and it's location on chunk servers. Chunkservers stores the chunks locally as linux file. Chunks are replicated per region in file namespace on different chunkservers, with default replication of 3. Master periodically exchanges heart beats with chunkservers and re-replicates chunks incase of chunkserver failures. Clients implement FS API and interacts with master and chunkserver. Client fetches metadata from master, and caches it locally. It reaches out to chunkserver directly for all data communication. 

GFS does not implement POSIX API, so there's no need for integration with linux v-node. Chunks are stored locally as linux files and OS buffer cache suffices the caching needs. No additional data caches are maintained either on client or chunkserver. 

Client caches the metadata information for short interval, till expiry or file gets reopened. Since chunksize is fixed, client calculates chunk index based on filename and offset. Master sends chunk handle & locations of all replicas which contain the chunk. For reads, client reaches out to closed replica. For performance reasons, client can request information about multiple chunks in the same request. Master generally sends information about subsequent chunks in the same response. 

Chunks are stored as 64 MB size plain linux file, which is larger than traditional file system. To make efficient use of disk, it's space is allocated lazily (lazy space allocation), ie, space is not allocated on disk if there's no data. There are many advantages of using a big chunk size - there's less interaction with master, persistent TCP connection with chunkserver, instead of frequently connecting new chunkservers, size of metadata on master is small, and clients themselves can cache multi TB file metadata in memory easily.   

One major disadvantage of using big block is, if there is a small file (size less than chunksize), it could face contention if multiple clients request the same file. In general, this is not the common, since files generally span multiple chunks, and client streams data from multiple servers. A way to mitigate could be to increase replication of such files, so request could span to different chunkservers and distribute load. 

There is single master, which stores all it's metadata in memory. Metadata stored by master includes:
- Mutations to file namespace
- Mapping of files to chunks
- Mapping of chunks to location of chunk replicas 
The first two are persisted to disk as operational log (WAL). Last one is not persisted to disk, but fetched on startup and everytime a chunkserver rejoins. The reason for this is, a chunkserver has sole ownership over which chunks it has locally. Chunks could get corrupted or disks could fail, and keeping this info in sync with master is futile. 

Storing metadata in memory allows master to do quick scans for various needs. And also serialize critical operations. 

Limitation is that file system is limited by how much data can be stored in RAM. In reality, data stored is effectively compressed, only 64B is stored per 64MB chunk. And it's not a serious limitation. And RAM can be increased very easily if required. 

For fault tolerance, master's operational logs are replicated on remote server as well. And each request is successfully only if log was written on all the servers.  In case of master failures, we can easily promote any of these servers as master, since they have the same data. To minimize the startup time, logs are checkpointed in background, so that on restart, it just have to read logs from last checkpoint. Checkpoints are B+ tree, which can be directly mapped to memory.

## Guarantees

**Consistent**: a file region is said to be consistent if all client read the same data from all replicas
**Defined**: a file region is said to be defined if after mutation, the file is consistent and has the mutation performed entirely

Guarantees provided by GFS:
- Writes by single client are defined
- Concurrent writes by multiple clients are consistent (same data on all replicas), but can be undefined (writes by other clients can be interleaved in between)
- Failed writes make the region inconsistent (different replicas may store different data). Leads to data duplication. 

All replicas must write the record at same offset for the operation to be success. 

The onus on recovering from failed write is on client. Client can retry again, but the data may get duplicated. On reads, client has to account for:

- extra space, padding 
- duplicate records (if write fails)

Each record written contains checksum, so client can recover from such failures. 
## Leases
For writes, master grants a lease (expiry 60s) to one of the replica (primary), the serial order of writes to be applied is decided by primary replica. The expiry of lease is 60s, but replica can extend it indefinitely by piggybacking on heartbeat call. Master can revoke lease before it expires, for eg, when doing snapshotting to ensure no writes happen. 
## Sequence Diagram

- Client requests master for replicas (including lease owner) of a chunk. If no lease owner found, master grants lease to a replica. 
- Client caches the metadata provided for a short interval
- Client pushes data to nearest replica, which in turn pushes data to next closest replica and so on. 
- Once all replicas acks that data is received, client sends write request to primary. Request identifies data written earlier. Primary assigns serial order all writes (can be from multiple clients), it applies mutations in that order. 
- Primary requests secondaries to apply mutation in same serial order
- Secondaries responds write completed. 
- Primary replies to client, Any error encountered is propagated to client, and means write has failed. Client can retry the failed mutation again. 
- If mutation will overstep the current chunks boundary, primary pads the current chunk with space. It instructs the secondaries to do the same. And returns client to retry again with new chunk. 

## Data flow

Data and control requests are separated, as the goal is to fully utilize the available bandwidth. Machines have full duplex, allowing them to send and receive at the same time at rate without any throttling. TCP pipelining is used, to start sending immediately the data is received instead of waiting for whole record to be received. 

## Snapshot

GFS provides ability to take a quick snapshot of a file or directory. Uses the copy on write technique. When a snapshot is requested:
- Master revokes all leases for the chunks, to prevent any further writes
- Duplicates the metadata, pointing to the same chunks
- Master intercepts any writes on the region performs clone operation. It instructs the replicas to clone C to C' locally. Since data is copied locally rather than over network, this is highly performant. 
- Any changes are handled in usual fashion
## Master Operations

Unlike traditional FS, GFS does not maintain per dir data structure. It maintains a global lookup table, mapping a path to metadata. Read write locks per path node are used to serialize operations. For eg, if reading `/d1/d2.../dn/leaf`, it acquires, read locks on d1 to dn and write lock on leaf. Read lock prevents node deletion, renaming or snapshoting. This way master can be highly concurrent and work on multiple requests simulatenously. To prevent deadlocks, locks are acquired in same order in ns tree & lexicographical at same level. 
## Replica Placement

For new replicas, chunkservers which has below average disk space are chosen. This equalizes disk utilization for the whole cluster. Servers are distributed over mutiple racks, to account for power and switch failures on a rack. On chunk server failures, master rereplicates the chunks on new servers, instructs them to clone from primary. Master does periodic rebalancing to keep cluster in good shape. 
## Garbage Collection

When a file or dir, is deleted:
- master logs the operation
- file is renamed to a hidden file with deletion timestamp
- during regular scan, it removes metadata for hidden files older than 3 days
- On every heartbeat, chunkserver, replies the chunks it has. Master replies chunks that are free to be deleted. 

Each chunk has a version number. The highest version is considered up to date. All other stale replicas are gc'd. 
## High Availability

Master logs are replicated on remote servers for each request. Due to checkpointing, master can be restarted within seconds. If machine/disk failure happen, a new master can be started on one of the remote servers.
## Data Integrity

Each 64 KB block in chunk is checksummed. If chunkserver detects corruption, it doesn't propagate the corrupted data, and reports error. 
## Questions
- 
## Related
- [](%5D)
