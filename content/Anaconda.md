---
title: Anaconda
updated: 2025-09-07 13:20:21Z
date: 2025-09-05 10:05:21Z
tags:
  - osinstall
share: true
---

**Source**: https://anaconda-installer.readthedocs.io/en/latest/user-guide/boot-options.html

Anaconda is the OS installer for RHEL based systems. 
### SSH to server for troubleshooting
(This only works if kernel arg: `inst.sshd` was set while live booting OS)
```
ssh root@server-ip

tmux attach

check ks logs: /var/run/install/ks.cfg
```

### Retry anaconda installer from failed server

```
anaconda --kickstart /path/to/ks.cfg
```

## Questions
- 
## Related
- [](Anaconda%5D)
- [](Anaconda%5D)
- [](Anaconda%5D)
- [](Anaconda%5D)