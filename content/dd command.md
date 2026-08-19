---
title: dd command
date: 2026-04-08
tags:
  - tooling
  - storage
  - 
share: true
---

**Source**: 

- if 'if=' not present it reads from stdin
- if 'of=' not present it writes to stdout

- bs = block size, default 512 bytes, change to 1 byte if you want to write single byte
- count = no. of block size bytes to write for eg if bs=1, count=4 will write 4 bytes
- seek = **write** at seek position to block size * number 
- skip = skip block size * number while **reading**

```
$ printf '🐱' | dd of=/dev/xvd1 
$ dd if=/dev/xvd1 count=1 2> /dev/null | hexdump -C

$ printf "$(dd if=/dev/xvd1 bs=1 count=4 2> /dev/null)\n"

$ printf '🐱' | dd of=/dev/xvd1 bs=1 seek=4

$ printf "$(dd if=/dev/xvd1 bs=1 count=8 2> /dev/null)\n"
```

## Questions
- 
## Related
- [](dd%20command%5D)
- [](dd%20command%5D)
- [](dd%20command%5D) 
- [](dd%20command%5D)