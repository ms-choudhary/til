# Wake On Lan (WOL)
Wake on LAN (WOL) is a protocol that enables you to wake up a computer/server remotely by a sending a ethernet packet. 

This has to be enabled in BIOS. Find where this is on our asrock minipc #question. 
For this, the NIC card has to constantly listen to all broadcast messages for magic packet. 

Since this works on hardware layer, it works regardless of OS etc. Only ethernet supports this feature. 

Works on a server in standby mode, ie, OS shut down normally with power supply still connected. Goes into ACPI S5 state, and it still receives standby power to listen on ethernet. 

### Magic packet

Magic packet is broadcasted on UDP ports 0, 7, 9 etc. Magic packet consists of 6 bytes of 0xFF followed target MAC address to wake up (repeated 16 times). This is because NIC receives stream of bytes without start and end. And checking for this pattern allows it to reliably and efficiently identify the MAC address. 

### Limitations

Packet has to originate from the network the server is in.  Doesn't really matter on what layer the packet is received, data link or ip, all the NIC hardware cares for is magic packet. 

## Sources
- 
## Related
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)