# Networking Modes in UTM

You can run apple virtualization VMs in two networking modes on UTM:

- Bridged networking
    - This adds the VM on the same network as your mac, although this works, there're few problems:
        - if you're connected to wifi, mac bridge might silently drop ARP packets leading to lossed connectivity intermittently.
        - You're now dependent on the wifi, if you disconnect wifi, you mysteriously lose connectivity
- Shared networking
    - despite what this name suggest, you cannot reach VM1 to VM2
    - adding forwarding config on mac doesn't work
    - and this is how this is supposed to be, refs:
		- https://github.com/utmapp/UTM/issues/4448
		- https://github.com/utmapp/UTM/issues/6975
## Questions
- This needs more details to trust the information listed. #question  
## Related
- [How connection works for two containers on same host?](/notes/networking/container-networking.md#How%20connection%20works%20for%20two%20containers%20on%20same%20host?)