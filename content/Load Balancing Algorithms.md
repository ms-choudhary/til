---
title: Load Balancing Algorithms
date: 2026-05-06
tags:
  - networking
  - http
share: true
---
Things you care about in load balancing, least packets drops, and low latency. 
## Request Queues on servers 

Different servers work differently, they start listening on port. Some create a fixed set of workers (process) at bootstrap, others create new process/threads per request. They can implement request queues where packets arrive, and workers pick it from. Packet is dropped if queue is full. This increases per request latency, as packets have to wait in queue before they can be processed.

In golang, a new go routine is created for every request. In this case, server is limited by resources rather than queue length.

## Centralised algorithms
### Round Robin

Most common default. Requests are routed to backend servers in uniform round robin fashion.

Drawbacks: In real world, all backend servers are **not equally powerful** and all request are **not equally expensive**, namely request & server variance. 
### Weighted Round Robin (WRR)

Humans tag each server with specific weight, and requests are served based on that weight. This **handles server variance**, but not request. This has better latency. 

Drawbacks: It's hard to come up with single digit number. It requires extensive benchmarking of servers. Adding human to the loop for every weight change can be a recipe for disaster. It doesn't account for request variance. 
### Dynamic Weighted Round Robin

Variant of WRR, it calculates the weights dynamically based on server metrics like latency. Since LB sits between client and server, it can track request latency from server. Weight is calculated dynamically based on that. 

**Works only on centralized load balancer**. 
### Least Connection

LB sits between client and server, knows server statistics like active connections, latency per server. In least connection, it prioritises servers with least active connections. Simple to calculate/maintain and quite effective. This **handles both server & request variance**. Hence it's a great default for most workloads. 

Requests are only dropped, when all of backend servers are overloaded. However it has slightly higher latency compared to WRR. 

**Works only on centralized load balancer**. In distributed load balancers, no single LB has full info of how many active connections are open on backend. 
### Peak Exponentially Weighted Moving Average (PEWMA)

Mix of Least connection & Dynamic Weighted RR. Tries to optimise for lower latency & better overload. 
### Drawbacks of centralised load balancing

- Single point of failures
- Scaling is only vertical, and can be very costly

## Distributed algorithms
### DNS Round Robin

No load balancer required. Endpoint resolves differently for each client. Works well in large system with homogenous requests.

Drawbacks: No health checks, backends cannot go down. Clients can override TTL and cache results for much longer. 

### Power of two random choices

Perfect distributed load balancing requires sharing current server loads with all load balancers. Overhead of constantly sharing this info is high. If this info is cached and synced periodically, it leads to herding of connections on a quiet backend for much longer, then cool down. So servers move from quiet -> busy -> quiet etc. 

In best of 2, you pick two backends randomly. Then, pick the one with low load. This works effectively even with cached info. 

## Sources
- https://samwho.dev/load-balancing/
- https://brooker.co.za/blog/2012/01/17/two-random.html
## Related
- [](Load%20Balancing%20Algorithms%5D)