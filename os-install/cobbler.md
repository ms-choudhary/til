# Cobbler

**Source**: 

Cobbler is a tool used for provisioning bare metal servers.

### Add cobbler system

```
cobbler system add --name="k8s1ny-w-19.indexww.com" --hostname="k8s1ny-w-19.indexww.com" --profile="K8S-CP-R9" --interface=p1p1 --ip-address=10.129.0.22 --mac=64:9D:99:B2:2F:C8 --static=1 --netmask=255.255.255.0 --gateway=10.129.0.250 --name-servers="192.40.39.191 1.1.1.1"  --name-servers-search="indexexchange.com casalemedia.com indexww.com"
```

## Questions
- 
## Related
- [anaconda](/os-install/anaconda.md)
- [initrd](/os-install/initrd.md)
- [dhcpd](/os-install/dhcpd.md)
- [idrac-racadm](/os-install/idrac-racadm.md)