---
title: Configuring systemd-resolved for DNS
updated: 2026-03-04 13:23:23Z
date: 2025-10-15 09:09:44Z
tags:
  - tooling
  - systemd
  - needs-work
share: true
---

**Source**: 

- Install
```
apt install systemd-resolved
```

- Global options `/etc/systemd/resolved.conf`
```
DNS=1.1.1.1 100.100.100.100
Domains=taildace6.ts.net
DNSStubListener=no
```

- Symlink `/run/systemd/resolve/stub-resolv.conf` to `/etc/resolv.conf`

```
ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

- Restart systemd-resolved

```
systemctl restart systemd-resolved
```

## Questions
- What's the difference between different types of dns configuration tools in linux? #question
	- https://tailscale.com/blog/sisyphean-dns-client-linux
- What are the implications of setting dns config via systemd? #question  
	- https://man7.org/linux/man-pages/man8/systemd-resolved.service.8.html
## Related
- [](%5D)
