---
title: Containers
date: 2026-03-31
tags:
  - container
  - tooling
  - linux
share: true
---
**Source**: 

### What?

- container is a group of linux processes running isolated in separate namespace
### Simple container in bash

(Only works on linux) [bit.ly/containers-arent-magic](http://bit.ly/containers-arent-magic)

```bash
# download the image
wget bit.ly/fish-container -O fish.tar

mkdir container-root; cd container-root

# unpack image to directory
tar -xf ../fish.tar

# generate random cgroup name
cgroup_id="cgroup_$(shuf -i 1000-2000 -n 1)"

# make a cgroup & set CPU/mem limits
cgcreate -g "cpu,cpuacct,memory:$cgroup_id"
cgset -r cpu.shares=512 "$cgroup_id"
cgset -r memory.limit_in_bytes=1000000000 "$cgroup_id"

# use the cgroup
# make + use some namespaces
# change root dir
# use the right /proc
# change hostname
# & start fish
cgexec -g "cpu,cpuacct,memory:$cgroup_id" \
  unshare -fmuipn --mount-proc \
  chroot "$PWD" \
  /bin/sh -c "/bin/mount -t proc proc /proc && hostname container-fun-times && /usr/bin/fish"
```
    
### Image
- Image is a tarball of a filesystem

![](Containers)

- Image can have multiple layers (to save common files from being downloaded again)
- Each layer is a directory of files
- Writes, when the container is run, goes to a temporary layer (which get's deleted when container is stopped, so to persist writes you need to mount a volume from outside)
- Overlay filesystems
	- Linux supports a filesystem comprising of different layers, known as Overlay Filesystem
	- How it works?
	
	```bash
	# lowerdir list of all readonly dirs
	# upperdir list of dir where writes should go
	# workdir internal use, empty
	# /merged target merged directory
	mount -t overlay overlay -o lowerdir=/lower,upperdir=/upper,workdir=/work \
	 /merged
	```
	
### Container Registry
- It's a HTTP server which serves images
- It lets you download only layers you need
### Linux kernel features which make containers work
#### pivot_root
- set's process's root directory to directory which contains image files
- chroot, which is typically used to change the root directory, is less secure, because original files are still there (you can access if you're root)
- containers generally use `pivot_root` instead. with this you can unmount old filesystem, so it's impossible to access them
#### cgroups
- One problem with traditional systems, is if you club different application in a instance, one application could end up using all resources thus throttling the other.
- cgroup is a group of process, all process in a container belong to same cgroup
- cgroup can have memory/CPU limits per group (all process in a container share those resources)
- If a process uses more memory then limit, it's OOM killed
- If a process uses more CPU then limit, it's throttled
- cgroups track these resources `/sys/fs/cgroup`
#### namespaces
- Is how you isolate the containers from the host
- Default namespace (host) is where things run outside a container
- Each process can have any combination of namespaces (eg, using host network namespace but it's own mount namespaces)
- To list namespaces for a process (`lsns -p <PID>`) or (`ls -l /proc/<PID>/ns` )
- How to create namespace
	- Child processes inherit the namespace from it's parent
	- Tools
	
	```bash
	# run in new network namespace
	unshare --net COMMAND
	
	# list all namespaces
	sudo lsns -p <PID> or ls -l /proc/PID/ns
	
	# run a command in PID's ns
	nsenter -t PID --all COMMAND
	```
	
- Different types of namespace (each ns has a man page, eg, `man network_namespaces`)
##### pid
- same process has different PIDs in different ns

![](Containers)

- if PID 1 gets killed, every process in the ns is killed
##### user
- it's a security feature, where you can map root user inside container to unprivileged user in host
- in user namespace, UIDs are mapped to host UIDs, unmapped users are shown as `nobody`
##### network
- created by 
```
ip netns add <name>
```
- has separate virtual interfaces for containers (usually two, loopback & normal)
- physical network card is in host network namespace
- other namespaces are connected to the host via bridge
- containers are assigned private IPs
- cloud providers have systems to make containers IPs work ("elastic network interface")
#### capabilities
- process needs to have capabilities (in addition of being root) to get work done
- check 
```
man capabilities
```
- `CAP_SYS_ADMIN` is like admin
- `CAP_NET_ADMIN` allow changes to network settings
- list capabilities for a PID
```
getpcaps PID
```
- `getcap` / `setcap` system calls to set/get capabilities
#### seccomp-bpf
- used to block certain system calls that process can execute (docker does this)
- seccomp-bpf lets you run a function before each system call
- this function decides if the sys call is allowed
- you can set a whitelist for a process

### Things you can configure while starting a container
- map a port inside container to the host
- mount directories from the host
- set capabilities
- add seccomp-bpf filters
- set memory & CPU limits
- use host network namespace


### Container security

Containers are advisable only for trusted workloads. Security failure in containers happen due to following:
#### Mis configuration

- Running as privileged containers, effectively removes all guard rails. It basically runs as root. 
- Mounting docker socket in containers (`/var/run/docker.socket`), allows it to create privileged containers, hence gives access to root. 
- Writable sys and /proc/sys, these expose kernel controls
- Writable dir, bind mounted inside containers. 
- Adding broad capabilities, eg `CAP_SYS_ADMIN`
- Joining host namespaces, eg `--pid=host` or `--net=host`
- Device passthrough (for eg like gpu), can expose raw kernel interfaces. 

#### Shared host kernel

Containers share the same kernel as host. Even if there's no misconfiguration, any kernel bug in the allowed syscalls, filesystem path or netstack behaviour can be triggered from inside the container. For eg, ioctl syscall has huge attack surface. 

Apart from misconfiguration and kernel bugs, bugs in container runtime also impact security. 

## Questions
- 
## Related
- [](Containers%5D)
- [](Containers%5D)