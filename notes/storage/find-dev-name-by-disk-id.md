# Find device name by disk id

`/dev/disk` contains symlinks to actual device name:
- by-id
- by-diskseq
- by-label
- by-partuuid
- by-path
- by-uuid

```
$ ls -l /dev/disk/by-id/
total 0
lrwxrwxrwx 1 root root  9 May  7 06:32 ata-INTEL_SSDSC2BX200G4R_BTHC629105S3200TGN -> ../../sdb
lrwxrwxrwx 1 root root 10 May  7 06:32 ata-INTEL_SSDSC2BX200G4R_BTHC629105S3200TGN-part1 -> ../../sdb1
lrwxrwxrwx 1 root root 10 May  7 06:32 ata-INTEL_SSDSC2BX200G4R_BTHC629105S3200TGN-part2 -> ../../sdb2
```

## Sources
- 
## Related
- [linux-dev-naming](inbox/in-progress/linux-dev-naming.md)