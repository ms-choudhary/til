# DHCPD

**Source**: 
### Leases 
- leases are stored at path: `/var/lib/dhcpd/dhcpd.leases`
### Configuration

DHCPD (isc-dhcpd) sample configuration:
```
ddns-update-style interim;

allow booting;
allow bootp;

ignore client-updates;
set vendorclass = option vendor-class-identifier;

option system-arch code 93 = unsigned integer 16;

subnet 10.203.32.64 netmask 255.255.255.192 {
     option routers             10.203.32.126;
     option domain-name-servers 10.199.1.240;
     option subnet-mask         255.255.255.192;
     range dynamic-bootp        10.203.32.65 10.203.32.100 ;
     default-lease-time         1800;
     max-lease-time             3600;
     next-server                $next_server_v4;
     class "pxeclients" {
          match if substring (option vendor-class-identifier, 0, 9) = "PXEClient";

          # Legacy
          if option system-arch = 00:00 {
              filename "grub/grub.0";
          }
          # UEFI-32-2
          if option system-arch = 00:02 {
              # Not supported, no 32 bit UEFI grub executable
              filename "unsupported";
          }
          # UEFI-64-1
          else if option system-arch = 00:07 {
              filename "grub/grubx64.efi";
          }
          # UEFI-64-2
          else if option system-arch = 00:08 {
              filename "grub/grubx64.efi";
          }
          # UEFI-64-3
          else if option system-arch = 00:09 {
              filename "grub/grubx64.efi";
          }
          # armv7   (aka arm 32 bit)
          else if option system-arch = 00:0a {
              filename "grub/armv7.efi";
          }
          # aarch64 (aka arm 64 bit)
          else if option system-arch = 00:0b {
              filename "grub/grubaa64.efi";
          }
          else
          {
              # This will be used when Bootmode is set to Legacy Bios
              filename "pxelinux.0";
          }
     }
}

```

### Troubleshooting

DHCPD config consists of subnet definitions it looks out for. If a packet arrives from one of these subnets, it responds with DORA flow. 
It only listens on interfaces for which subnets are defined in configuration. If there's no subnet definition for interfaces, it fails to come up. 

If you don't see a packet arriving, ensure you've interface subnet added along with target subnet.  
## Questions
- 
## Related
- [cobbler](/notes/os-install/cobbler.md)
- [anaconda](/notes/os-install/anaconda.md)
- [Capture DHCP packets](/notes/networking/tcpdump.md#Capture%20DHCP%20packets)
