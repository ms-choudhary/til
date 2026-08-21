# SSH

### Forward tunnel

![[notes/_images/Pasted image 20260415210543.png|600]]

Service is **running on remote server**, and you're connecting to localhost on the client. 

```
ssh -L [bindaddress:]port:host:hostport target
eg
ssh -L 8000:localhost:8000 ixdev
```

host is resolved on the target server. In this case, any request on port 8000 on the client is forwarded to localhost:8000 on ixdev. 

```
ssh -L 8000:randomhost:8000 ixdev
```

In this case, any request on port 8000 on the client is forwarded to randomhost (resolved on ixdev) via ixdev.

#### How this works?

- When you run the ssh forward port-forward command, a tcp socket is open on client side for the port 8000. Nothing happens on the remote side yet. 
- When a new request comes for localhost:8000, it's multiplexed on the ssh encrypted tcp connection via different channel number. (eg, channel 1 etc)
- On the remote side, sshd receives handles the packets from channel 1, and forwards them to localhost:8000. 
- To the remote service (running on port 8000), it appears as if packet has arrived from localhost. To client service, it appears as if it's interacting with a local service. And tunnel is invisible to both. 

### Reverse Tunnel

![[notes/_images/Pasted image 20260415211658.png]]
Service is **running on local client**, and you're connecting to localhost on the vm. 

```
ssh -R [bindaddress:]port:host:hostport target

ssh -R 8000:localhost:8000 ixdev
```

Any request on port 8000 on remote VM is forwarded via secure channel to localhost:8000 running on local client. host is resolved on the local client.  

#### How this works?

- A tcp socket on port 8000 is open on the remote side. 
- Whenever any packets comes locally to 8000, it's multiplexed via secure channel to client side. 
- On the client side, it proxies the packet to service running on localhost:8000

### Remote Connection Hung
- If your connection to remote server is hung and you can't do anything: `Enter` `~` `.` This forces the client to close the connection. 
	- This doesn't work on nested ssh connections!

## Questions
- Explore how connection is established and a terminal is spawn in ssh. #question 
## Related
- [sshfs](/storage/sshfs.md)