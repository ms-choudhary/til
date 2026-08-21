# Setup socat proxy to remote host

TCP request on port 6443 is forwarded to remote-host:6443
```
docker run -d --name proxy6443 --restart unless-stopped -p 6443:6443 \
  alpine/socat \
  TCP-LISTEN:6443,fork,reuseaddr \
  TCP:remote-host:6443
```

## Sources
- 
## Related
- [network-load-balancing](inbox/in-progress/network-load-balancing.md)