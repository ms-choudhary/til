---
title: Redfish
date: 2026-05-14
tags:
  - osinstall
share: true
---
### Attach virtual media

You can attach an ISO to virtual media (like CDROM) on the server via redfish virtual media API. Generally requires license. BMC will download & present it as virtual CD ROM to the host OS/bios. 

### UEFI HTTP boot

Uses reliable TCP connection, instead of UDP (TFTP). Thus enables scalability & performance using http load balancer. Still requires functional DNS, DHCP, http servers. Just uses HTTP over TFTP. 

## Sources
- 
## Related
- [](Redfish%5D)