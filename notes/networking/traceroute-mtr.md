# Traceroute/ MTR

Traceroute uses incremental TTLs on IP packets to figure out hops on the network. TTL is decremented by one on every hop. Once TTL is zero, router sends back ICMP time exceeded. 

MTR is traceroute + ping. 

### Perform AS number lookup

```
mtr --aslookup yahoo.com
```