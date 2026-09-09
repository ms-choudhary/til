# Global Internet Routing

As a end user, we've very simplistic view of internet, we send a packet and it magically lands at google.com for example. "There's no real cloud, only other people's computers". 

Bulk of internet is still physically connected, with cables under the sea connecting continents. It uses a special cable known as [submarine communication cable](https://en.wikipedia.org/wiki/Submarine_communications_cable) , see the [map](https://www.submarinecablemap.com/) for the interconnections. 

### Level of connections

If you connect, two computers together, it's a point to point connection. 

If you connect multiple computers via LAN, they are part of same network in the broadcast domain. 

You use router to connect multiple such L2 networks. 

### Autonomous Systems

At high level, AS, is a bunch of networks grouped together. It could have multiple internal networks with independent IP address space. 

An AS can control a set of IP address.

Autonomous Systems Number (ASN) is assigned by IANA along with [ip-allocation](/notes/networking/ip-allocation.md).  

### Peering

![](/_images/internet.png)
Peering connects multiple such networks (AS) physically. This allows sharing routing info via bgp. Such connections are called peering points or internet exchange points (IXPs). These are strategically located in data warehouses across the globe. The central stars in above diagrams are the IXPs. 

Peering and ASN are public information available at [peeringdb](https://www.peeringdb.com/net/1903). Useful when you're planning to setup a datacenter. [building-datacenter](/notes/hardware/building-datacenter.md)

Not every network directly peers with others at public IXP, there're private connection as well. 

Also check [list of internet exchange points](https://en.wikipedia.org/wiki/List_of_Internet_exchange_points). 