---
title: qemu-guest-agent
date: 2026-05-26
tags:
  - virtualization
share: true
---
qemu-guest-agent runs inside VM, and basically is a communication channel between host and guest. It enables things like:
- Set guests system time
- Get information from the guests
- Read/write file
- Sync/freeze filesystems
- Suspend guests

It uses a virtio-serial channel, ie, a virtual serial port exposed to guest as a character device, this by passes the normal network stack entirely. On hosts side this is exposed as unix domain socket. 
### qemu-guest-agent configuration sample

```
[general]
daemonize = 0
pidfile = /var/run/qemu-ga.pid
verbose = 0
method = virtio-serial
path = /dev/virtio-ports/org.qemu.guest_agent.0
statedir = /var/run
```


## Sources
- 
## Related
- [](%5D)