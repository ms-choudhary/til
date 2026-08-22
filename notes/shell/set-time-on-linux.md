# Set time on linux

**Source**: 
### Set systemwide timezone on linux

`/etc/localtime` symlinks to timezone file in /usr/share/zoneinfo. Changing the link to different timezone changes the systemwide timezone info. 
```
msc@debian:~$ ls -l /etc/localtime
lrwxrwxrwx 1 root root 32 Nov 15 10:39 /etc/localtime -> /usr/share/zoneinfo/Asia/Kolkata
```

### Set system time on linux

```
date -s 'Sat Nov 23 15:12:58 IST 2024'
```

## Questions
- 
## Related
- [[]]

