# Explore remote drive via SSHFS

**Source**: https://man7.org/linux/man-pages/man1/sshfs.1.html

Lately I wanted to explore the external hard drive connected to my homelab mini pc for some photos I wanted to upload to immich.  Instead of manually unplugging and replugging the drive to my mac, I decided to use sshfs. 

From the manpage, 

> SSHFS allows you to mount a remote filesystem using SSH (more precisely, the SFTP subsystem). Most SSH servers support and enable this SFTP access by default, so SSHFS is very simple to use - there's nothing to do on the server-side.

It is based on FUSE filesystem. 
## Installation

### Debian/Ubuntu

```
apt install sshfs
```

### MacOS

Install Macfuse and sshfs from [macfuse](https://macfuse.github.io) site. It'll prompt to allow a system extension in system settings. Also a restart is required. 

## Usage

```
sshfs homelab:/var/homelab ~/Documents/mnt
```

Loads `/var/homelab` remote dir to `~/Documents/mnt`. 

You can then explore the files in finder. Finally to unmount:

```
umount ~/Documents/mnt
```

## Questions
- Explore fuse fs #question 
- This reduces the iops on the backup drive, and you've to remount it again #question 
## Related
- [dd](/notes/storage/dd.md)
- [ssh](/notes/ssh/ssh.md)