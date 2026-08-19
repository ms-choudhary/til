---
title: Keepalived
date: 2026-04-29
tags:
  - networking
share: true
---
It's a linux daemon which provides high availability and load balancing for a backend group of servers. It's built on top of VRRP (Virtual Router Redundancy Protocol) and IPVS (IP Virtual Server). 

### VRRP

The main objective of VRRP is to provide **high availability** of service to clients. Instead of exposing IP of a single server to users, VIP (virtual IP) is exposed which is shared by multiple servers.

One of the server is elected as Master (based on priority set in configuration), and all the traffic is routed through it. Periodically, master sends heartbeat to other backup servers. In case, a heartbeat is skipped, one of the other backup server is elected as master, and starts serving the traffic via the same virtual IP. The failed server is removed from the pool. The client/user is unaware of this change, since it still connects on the same IP.

### IPVS

IPVS is a kernel mechanism to distribute connections to backend servers, basically a **L4 load balancer**. It supports scheduling based on round robin, least connections or weighted traffic to backend servers.  


## Sources
- 
## Related
- [](Keepalived%5D)
