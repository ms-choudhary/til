# IPv6

IPv6 uses 128 bits for addressing (compared to 32 bits of IPv4). To give an idea of how vast that is, you can give every atom in human body for the whole world population [6 address](https://www.wolframalpha.com/input?i=2%5E128+%2F+%28world+population+*+atoms+in+human+body%29+). 

### Representation

Instead of dotted notation used by IPv4, IPv6 are represented as 8 16 bit fields of case insensitive hexadecimal colon separated words. 

Eg, 
```
2001:4998:0124:1507:0000:0000:0000:F000
```

To shorten this further, 
- You can drop leading zeros
```
2001:4998:124:1507:0:0:0:F000
```
- You can replace successive zeros by `::`, but only once per address,
```
2001:4998:124:1507::F000
```

Loopback address are represented as: `::1`

In dual stack hosts, you can also have IPv4 mapped address, where last part is also the ipv4 address of the interface, eg:

```
::ffff:74.6.143.25
```

Ports are represented as:

```
[2001:4998:124:1507::F000]:443
```

### Address scopes

#### Link local address

All IPv6 address always has a link local scope address. Its generated on the host, using standard algorithm for the lower 64 bits, without requiring DHCP or any other network configuration. Packets with link local source/destination is not forwarded to other links. 

Within:
```
fe80::/10
```

#### Private Unique Local Address

Private IPv6 networks similar to [IPv4 Address blocks](/notes/networking/subnets.md#IPv4%20Address%20blocks). Not globally routed
```
fc00::/7 or fd00::/8
```

#### Global Address

Globally unique and routed by the internet. 


### Sipcalc

```
$ sipcalc fe80::/10
-[ipv6 : fe80::/10] - 0

[IPV6 INFO]
Expanded Address        - fe80:0000:0000:0000:0000:0000:0000:0000
Compressed address      - fe80::
Subnet prefix (masked)  - fe80:0:0:0:0:0:0:0/10
Address ID (masked)     - 0:0:0:0:0:0:0:0/10
Prefix address          - ffc0:0:0:0:0:0:0:0
Prefix length           - 10
Address type            - Link-Local Unicast Addresses
Network range           - fe80:0000:0000:0000:0000:0000:0000:0000 -
                          febf:ffff:ffff:ffff:ffff:ffff:ffff:ffff
```