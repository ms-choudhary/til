# Tcpdump

**Source**: 

### List interfaces

```
tcpdump -D
```
### Expression
- Check `man pcap-filter` for tcpdump expression syntax and fields

### Capture file
```
tcpdump -w capture.pcap -i any host google.com
```

### Capture DHCP packets
```
tcpdump -i any -vv -n port 67 or port 68
```

### Capture packets from specific mac address
```
tcpdump -i bond0.101 -n -vvv -e ether host 2c:ea:7f:89:d5:95
```
## Questions
- 
## Related
- [dhcpd](/os-install/dhcpd.md)