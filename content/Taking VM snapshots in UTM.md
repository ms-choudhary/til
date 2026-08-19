---
title: Taking VM snapshots in UTM
date: 2024-11-15 16:48:49Z
tags:
  - virtualization
  - tooling
  - macos
  - storage
share: true
---

**Source**: 

### Snapshots
You can locate the UTM data disk for a VM: `~/Library/Containers/com.utmapp.UTM/Data/Documents/Linux.utm/Data`, which is generally a qcow2 image. 

Take a snapshot with compression:

```
qemu-img snapshot F89035CE-DEF9-49D7-97F8-7EC0C2F3F9D9.qcow2 -c snapshot1

qemu-img snapshot F89035CE-DEF9-49D7-97F8-7EC0C2F3F9D9.qcow2 -l
```

To revert back the disk:

```
qemu-img snapshot F89035CE-DEF9-49D7-97F8-7EC0C2F3F9D9.qcow2 -a snapshot1
```

## Questions
- 
## Related
- [](Taking%20VM%20snapshots%20in%20UTM%5D)