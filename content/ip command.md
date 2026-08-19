---
title: ip command
date: 2026-04-07
tags:
  - networking
  - tooling
share: true
---

### Manually assign ip address to interface

```
ip addr add 10.118.16.4/26 dev eno1
```

`/24` is important, if not provided it'll default to `/32`

### Bring up/down a link

```
ip link set eno1 down
ip link set eno1 up
```
### Show the route taken for ip

Helpful when there're multiple interfaces

```
ip route get <ip>
```

## Questions
- 
## Related
- [](ip%20command%5D)
- [](ip%20command%5D)
