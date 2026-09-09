# IP Allocation

Internet Assigned Numbers Association (IANA) (administered by ICANN) oversees:
- global ip address allocation
- autonomous systems number allocation
- root zone management

### RIR
Except the private address space [IPv4 Address blocks](/notes/networking/subnets.md#IPv4%20Address%20blocks), it assigns large blocks of address space to Regional Internet Registry (RIR). Ex:
- AFRINIC
- APNIC
- ARIN (Americas)
- LACNIC (Latin America)
- RIPE NCC (Europe)

RIRs further assigns blocks to Local Internet Registries, which assign it to:
- Internet Service Providers (ISPs)
- Large Education Institutions
- Large Enterprises

ISPs can further delegate to other entities as they see fit. 

If you see an ip from AFRINIC, it can be misleading to infer that it originates from africa. Ip address are not bound by physical location, it just means the administrative ownership lies with AFRINIC. 

### Address Assignment

- /8 = RIR
- /16, /17, /18, /19 = LIR, ISPs, Large business
- /20 = Small ISPs, Large business
- /24 = LAN