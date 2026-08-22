# IDrac Racadm

iDRAC is a separate BMC chip, on dell, which integrates on the motherboard, and provides users to control a server remotely. You could build a similar feature with piKVM, [diy](https://docs.pikvm.org/v2/):
- Connect the video cable.
- Integrate circuit to motherboard power supply

With serial over lan, you can get serial console remotely for troubleshooting purposes. 
### Alias

```
alias myracadm="racadm -r 10.118.16.27 -u root -p calvin --nocertwarn"
```

### Check sel logs

```
/opt/ix/ops-bin/rracadm.sh -v db-vertica-vera-84.prod.tor3.indexww.com getsel -o
```

### Check cpu reset

```
/opt/ix/ops-bin/rracadm.sh bh2-prod-data-674.ix1.indexww.com lclog view -n 10 -k CPU
```

### Set first boot to pxe

```
racadm -r 10.118.16.3 -u root -p calvin set idrac.serverboot.firstbootdevice PXE
```

### pxe device

```
./racadm get BIOS.PxeDev1Settings.PxeDev1Interface

./racadm set BIOS.PxeDev1Settings.PxeDev1Interface <interface name, something like NIC.Slot.1-1>
```

### Powercycle

```
racadm -r 10.118.16.3 -u root -p calvin serveraction powercycle
```

### Jobqueue

```
myracadm jobqueue create BIOS.Setup.1-1 -r pwrcycle
```

### racreset

```
racadm racreset soft
```

### Pre-requisites for ssh, ipmi or webconsole

```
racadm set idrac.ipmilan.enable Enabled
racadm  set idrac.ssh.enable Enabled
racadm set iDRAC.WebServer.HostHeaderCheck Disabled
```
### Via ssh

```
ssh root@idrac_ip
ssh -o KexAlgorithms=curve25519-sha256 root@idrac_ip
console com2
```

ctrl + \ to exit
### System info

```
racadm getsysinfo
```

### Virtual media

Check [Attach virtual media](/notes/os-install/redfish.md#Attach%20virtual%20media)

Requires license. Although you can get trail enterprise license from dell website. Trial license can only be loaded once per server. After expiry you cannot add any other trial license. 

Connect 
```
myracadm remoteimage -c -l http://10.40.16.10:8080/bootc-almalinux-10.2-bootc-generic-iso-x86_64/bootc-almalinux-10.2-bootc-generic-iso-x86_64.iso
```

Set first boot device to Virtual CD:
```
racadm set iDRAC.ServerBoot.FirstBootDevice VCD-DVD
```

Check status:
```
myracadm remoteimage -s
```

Disconnect:
```
myracadm remoteimage -d
```
### Connectivity Check

```
racadm ping 10.40.16.10
racadm traceroute 10.40.16.10
```
## Sources
- 
## Questions
- 
## Related
- [cobbler](/notes/os-install/cobbler.md)
- [dhcpd](/notes/os-install/dhcpd.md)
- [redfish](/notes/os-install/redfish.md)
