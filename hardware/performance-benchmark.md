# Performance benchmark

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
- [[]]