# Grub

### Update kernel options via grub

- Edit file `/etc/default/grub` with necessary change
- Finally run `grub2-mkconfig -o /boot/grub2/grub.cfg` (on rhel, centos) or `update-grub` on debian, ubuntu
	- if it doesn't work try adding option `--update-bls-cmdline` to grub2-mkconfig
	- for efi the path could be different: 

## Sources
- 
## Questions
- 
## Related
- [initrd](/notes/os-install/initrd.md)
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)
