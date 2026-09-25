# Tailscale
### Enable ssh

On the node, 
```
tailscale set --ssh
```

Then you can ssh normally using server name (in tailnet):

```
ssh root@dev-web-nyc1
```

### Exit node

By default, tailscale only add specific routes, so only traffic to other tailnet nodes goes via it, not entire traffic on the node. You can however, set a designated exit node, which then routes all local traffic via exit node. 

Use cases:
- Access sites not accessible in other locations (for eg home banks etc)