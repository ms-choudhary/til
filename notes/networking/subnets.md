# Subnets

IPv4 Address is 32 bit number, which is divided into network and host parts
```
[192.168.10] + [.98]
network      + host
```
Network part is also represented as: 192.168.10.0/24, `/24` represents the network bits also known as subnet mask. 

Hosts in same network are part of broadcast domain, meaning they don't require a router to communicate. They can communicate directly at L2 using switch. 

### IPv4 Address blocks

Whole of address space is divided into specific address blocks, by IETF & IANA, namely 
- private address spaces - 10.0.0.0/8, 192.168.0.0/16, 172.16.0.0/12 
- Loopback addresses to localhost - 127.0.0.0/8 
- Others

### Netmask

`/24` contains 2^8 = 256 address

```
$ ipcalc 192.168.10.0/24
Address:   192.168.10.0         11000000.10101000.00001010. 00000000
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111
=>
Network:   192.168.10.0/24      11000000.10101000.00001010. 00000000
HostMin:   192.168.10.1         11000000.10101000.00001010. 00000001
HostMax:   192.168.10.254       11000000.10101000.00001010. 11111110
Broadcast: 192.168.10.255       11000000.10101000.00001010. 11111111
Hosts/Net: 254                   Class C, Private Internet
```

Of these first and last address cannot be assigned to a host. First address represents the network itself. And last address is broadcast address, used for broadcasting to all hosts in the network. 

### Carve smaller subnets

```
$ ipcalc -s 24 64 48 192.168.10.0/24
Address:   192.168.10.0         11000000.10101000.00001010. 00000000
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111
=>
Network:   192.168.10.0/24      11000000.10101000.00001010. 00000000
HostMin:   192.168.10.1         11000000.10101000.00001010. 00000001
HostMax:   192.168.10.254       11000000.10101000.00001010. 11111110
Broadcast: 192.168.10.255       11000000.10101000.00001010. 11111111
Hosts/Net: 254                   Class C, Private Internet

1. Requested size: 24 hosts
Netmask:   255.255.255.224 = 27 11111111.11111111.11111111.111 00000
Network:   192.168.10.192/27    11000000.10101000.00001010.110 00000
HostMin:   192.168.10.193       11000000.10101000.00001010.110 00001
HostMax:   192.168.10.222       11000000.10101000.00001010.110 11110
Broadcast: 192.168.10.223       11000000.10101000.00001010.110 11111
Hosts/Net: 30                    Class C, Private Internet

2. Requested size: 64 hosts
Netmask:   255.255.255.128 = 25 11111111.11111111.11111111.1 0000000
Network:   192.168.10.0/25      11000000.10101000.00001010.0 0000000
HostMin:   192.168.10.1         11000000.10101000.00001010.0 0000001
HostMax:   192.168.10.126       11000000.10101000.00001010.0 1111110
Broadcast: 192.168.10.127       11000000.10101000.00001010.0 1111111
Hosts/Net: 126                   Class C, Private Internet

3. Requested size: 48 hosts
Netmask:   255.255.255.224 = 27 11111111.11111111.11111111.111 00000
Network:   192.168.10.128/27    11000000.10101000.00001010.100 00000
HostMin:   192.168.10.129       11000000.10101000.00001010.100 00001
HostMax:   192.168.10.158       11000000.10101000.00001010.100 11110
Broadcast: 192.168.10.159       11000000.10101000.00001010.100 11111
Hosts/Net: 30                    Class C, Private Internet

Needed size:  224 addresses.
Used network: 192.168.10.0/24
Unused:
192.168.10.224/27
```