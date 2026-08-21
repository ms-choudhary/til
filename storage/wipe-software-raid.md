# Wipe software raid

Wipe the filesystem on the raided drive, then stop raid
```
$ wipefs -a /dev/md127

$ mdadm --stop -f /dev/md127
```

Finally wipe the partitions

```
wipefs -a /dev/sda
wipefs -a /dev/sdb
```

## Sources
- 
## Related
- [[]]