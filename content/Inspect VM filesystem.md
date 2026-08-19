---
title: Inspect VM filesystem
updated: 2026-03-04 12:59:10Z
date: 2026-03-04 12:59:02Z
tags:
  - virtualization
  - tooling
  - storage
share: true
---
**Source**: https://linux.die.net/man/1/guestfish

To inspect files inside VM disk (qcow2, img or other kinds), install guestfish:

```
apt install libguestfs-tools
```

```
guestfish 
> add-ro debian.qcow2
> run
> help mount-ro
```

Type help gives you what you should do next. You can copy files to host via `copy-out /file/in/qcow2 /host/dir/`

## Questions
- There's a way to install os by using qcow2 image (without running the installer). How does that work? #question 
## Related
- [](Inspect%20VM%20filesystem%5D)
- [](Inspect%20VM%20filesystem%5D)
