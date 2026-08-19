---
title: Package Management
date: 2024-11-24 03:52:22Z
tags:
  - tooling
  - linux
share: true
---
### Debian dpkg

Debian `.deb` package is an `ar` archive consisting of 2-3 nested tar archives, along with maintainer scripts (eg, `preinst`, `postinst`, `prerm`, `postrm`) which runs arbitrary shell scripts. 

```
# list inventory of packages and their version installed
$ dpkg -l

# List file contents of a package
$ dpkg -L tcpdump

# Reverse lookup, which package provides this file
$ dpkg-query -S /usr/bin/dig
```

Packaging systems can keep track of dependencies only if all softwares are installed via package management. If for eg, awscli was installed outside package management, dpkg won't know if upgrading python will break awscli. 

gpg keys are used to check the signature to validate if package was signed by trusted entity. 

### Fedora rpm

```
# list inventory
$ rpm -qa


# list content 
$ rpm -ql tcpdump

# verify integrity of a package; if it was modified
$ sudo rpm -V sudo
$ sudo rpm -Va  # all packages
```

### Netbsd vulnerability for packages

```
$ pkg_admin -V -v fetch-pkg-vulnerabilities
$ pkg_admin audit
```

### Alpine apk

APK is both a package manager for alpine and format of package on the disk. It's simple gzipped tarball consisting of control segment, data segment & signature. 

```
# Plain text file with list of packages installed
$ cat /etc/apk/world

# Repository file
$ cat /etc/apk/repositories

# DB of installed packages
$ cat /lib/apk/db/installed
```

```

# list installed packages
$ apk list --installed

# Full info about a package
$ apk info -a busybox

# Files owned by package
$ apk info -L busybox

# Dependencies of a package
$ apk info -R busybox

# Which package owns a file
$ apk info --who-owns /bin/ls
```


## Sources
- 

## Questions
- 
## Related
- [](Package%20Management%5D)
