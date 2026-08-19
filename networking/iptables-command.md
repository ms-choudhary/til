# iptables command

**Source**: 
### Show iptables stats

```
iptables -nvL [chain]
or
iptables --numeric --verbose --list [chain]
```
### Dump rules to stdout

```
iptables-save
```
### Show dropped packets by iptable rules

```
$ iptables -A INPUT -j LOG --log-prefix "IPT-DROP-INPUT: " --log-level 4
$ journalctl -f | grep "IPT-DROP-INPUT"
Apr 07 08:36:37 ops-fr-1.dcaux.indexww.com kernel: IPT-DROP-INPUT: IN=bond0 OUT= MAC=4c:d9:8f:3d:7c:f3:00:2c:c8:7a:69:bf:08:00 SRC=85.217.140.29 DST=185.80.39.238 LEN=52 TOS=0x00 PREC=0x00 TTL=54 ID=62016 PROTO=TCP SPT=41560 DPT=38472 WINDOW=65535 RES=0x00 SYN URGP=0

```
### Make permanent changes to iptables

#### On RHEL

```
$ vim /etc/sysconfig/iptables
$ systemctl restart iptables
```
## Questions
- 
## Related
- [ip-command](/networking/ip-command.md)
- [container-networking](/networking/container-networking.md)