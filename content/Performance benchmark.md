---
title: Performance benchmark
updated: 2026-03-04 13:31:39Z
date: 2025-09-27 07:59:45Z
tags:
  - tooling
  - linux
share: true
---
**Source**: 
- https://it-notes.dragas.net/2025/09/19/freebsd-vs-smartos-whos-faster-for-jails-zones-bhyve/
- https://manpages.debian.org/testing/sysbench/sysbench.1.en.html

## CPU performance
```
sysbench --test=cpu --cpu-max-prime=20000 run
```

## Memory performance
```
sysbench --test=memory run
```

## Questions
- 
## Related
- [](%5D)