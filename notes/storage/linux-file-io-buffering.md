# Linux File IO Buffering

When you read or write to files via read/write syscalls, it doesn't directly initiate access to disk. Instead, first the data is copied to in memory kernel buffer, known as buffer cache. Then at some later point, kernel writes (flushes) the buffer to disk. If in between, some other process reads the same file, kernel provides it from the buffer cache. 

Reads are buffered to cache as well, so kernel first reads the data from disk to buffer cache. Calls to reads are served from the buffer cache. Kernel performs read ahead for sequential reads. 

The aim of this to make read/write be performant and return fast, rather than waiting for slow I/O. 

There's no upper limit on the size of the buffer cache. It solely depends on:
- availability of physical memory
- demand for other purposes 

Even though reads and writes are buffered in kernel, every time you invoke syscall, there's a performance penalty, to overcome this, the data is also buffered in stdio c library. 

Data is buffered in large blocks to reduce number of sys calls. You can force the data in stdio to be written to kernel buffer, by calling `fflush()` lib call. 
![](/_images/linux-file-buffering.jpeg)
To flush the kernel buffer to disk, use `fsync()` call. It returns only when all the data & metadata is flushed to the disk. Used by databases for journaling operations. 

For direct IO (without buffer) specify `O_DIRECT` flag when opening file. 

## Sources
- 
## Related
- [gfs](/notes/system-design/gfs.md)