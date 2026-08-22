# Anaconda

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
- [cobbler](/notes/os-install/cobbler.md)
- [dhcpd](/notes/os-install/dhcpd.md)
- [initrd](/notes/os-install/initrd.md)
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)