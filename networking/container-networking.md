# Container Networking

**Source**: https://www.youtube.com/watch?v=6v_BDHIgOY8

- Check [[notes/container/containers#network]]
- All containers have virtual ethernet(`veth`)interface attached
- `veth` 's are created in pair's. For container networking, one part of the veth is in network namespace.
- `bridge` interface is common connecting link. In a bridge, one part of it remains in host, other's are connected with multiple veth interfaces(container's). Bridge generally has a range of IP addresses (equivalent to each container's ip).
- Apart from above connections `veth` & `bridge` all other connection depend on routing
### How connection works for two containers on same host?
- Hint: it uses bridge
- All communications from containers are routed via bridge to host
- All host communications are routed to containers via bridge
	
	![](/_images/container-networking-same-host.png)
	

```bash
echo "Creating the namespaces"
sudo ip netns add $CON1
sudo ip netns add $CON2

echo "Creating the veth pairs"
sudo ip link add veth10 type veth peer name veth11
sudo ip link add veth20 type veth peer name veth21

echo "Adding the veth pairs to the namespaces"
sudo ip link set veth11 netns $CON1
sudo ip link set veth21 netns $CON2

echo "Configuring the interfaces in the network namespaces with IP address"
sudo ip netns exec $CON1 ip addr add $IP1/24 dev veth11 
sudo ip netns exec $CON2 ip addr add $IP2/24 dev veth21 

echo "Enabling the interfaces inside the network namespaces"
sudo ip netns exec $CON1 ip link set dev veth11 up
sudo ip netns exec $CON2 ip link set dev veth21 up

echo "Creating the bridge"
sudo ip link add name br0 type bridge

echo "Adding the network namespaces interfaces to the bridge"
sudo ip link set dev veth10 master br0
sudo ip link set dev veth20 master br0

echo "Assigning the IP address to the bridge"
sudo ip addr add $BRIDGE_IP/24 dev br0

echo "Enabling the bridge"
sudo ip link set dev br0 up

echo "Enabling the interfaces connected to the bridge"
sudo ip link set dev veth10 up
sudo ip link set dev veth20 up

echo "Setting the loopback interfaces in the network namespaces"
sudo ip netns exec $CON1 ip link set lo up
sudo ip netns exec $CON2 ip link set lo up

echo "Setting the default route in the network namespaces"
sudo ip netns exec $CON1 ip route add default via $BRIDGE_IP dev veth11
sudo ip netns exec $CON2 ip route add default via $BRIDGE_IP dev veth21
```
	
### How connection works between two containers on different host but same subnet?
- Hint: It uses static ip routes
- Prerequisite: Host and containers are able to communicate
- Bridge on a host is allocated range of IP address (subnet)
- If request is for bridge on other node, request is forwarded to the node

![](/_images/container-networking-diff-host-same-subnet.png)
	
### How connection works between two containers on different host on different subnet?
- Case of overlay networks
- In this case, nodes are linked but not on same network. Could be on internet. Could be different zones, etc
- If other node is not next hop(i.e., different subnet), routing rules just on nodes won't work, unless applied to all routers in between.
- Prerequisite: Node should be able to communicate to each other
- Hint: Use `tun` interface to hide a proxy, such that, data routed to `tun` is packaged in udp packet and send to appropriate node. Same process is followed on other node & data out from `tun` is fed to `bridge`

![Container Networking Diff Host Diff Subnet](/_images/container-networking-diff-host-diff-subnet.png)
## Questions
- 
## Related
- [containers](/container/containers.md)
- [iptables-command](/networking/iptables-command.md)
- [ip-command](/networking/ip-command.md)