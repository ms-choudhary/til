# /proc filesystem

It's a virtual filesystem which provides interface to kernel internal data structures, which looks like traditional files and dirs. It's created on the fly by the kernel as process access them. 
### Important files

#### /proc
- /proc/version - kernel version
- /proc/self - a process can access it's own proc pid dir at /proc/self
- /proc/net - status info about networking & sockets
- /proc/sys/fs - settings related to filesystems
- /proc/sys/kernel - kernel settings
- /proc/sys/net  - networking settings
- /proc/sys/vm - memory management settings
#### /proc/PID

- /proc/PID/status - contains runtime info about the process
- /proc/PID/cmdline - command line arguments used to invoke
- /proc/PID/cwd - current working dir of the process
- /proc/PID/environ - environment variables 
- /proc/PID/exe - symlink to executable binary 
- /proc/PID/fd  - symlink to files opened  
- /proc/PID/maps - memory mapping
- /proc/PID/mem - process virtual memory
- /proc/PID/mounts - mountpoints for this process
- /proc/PID/root - symlink to the root dir
- /proc/PID/task - one subdir per thread

![](/_images/proc-fs-files.jpeg)

### Boot ID

`/proc/sys/kernel/random/boot_id` holds random id which changes at every boot and is assigned quite early in the boot process. 

It is used by systemd & journalctl to track separate logs on reboot. 

## Sources
- 
## Related
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)