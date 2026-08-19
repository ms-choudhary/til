# Initrd

## Extract

```
xzcat initrd.img | cpio -id

-i extract
-d create dirs
```

## Check content

```
# show content of initramfs of current kernel
lsinitrd

# show content of specific initramfs file
lsinitrd path/to/initramfs.img
```

## Sources
- 
## Questions
- 
## Related
- [cobbler](/os-install/cobbler.md)
- [anaconda](/os-install/anaconda.md)
- [inspect-vm-filesystem](/virtualization/inspect-vm-filesystem.md)
- [dd](/shell/dd.md)
- [grub](/os-install/grub.md)
- [booting-linux-on-x86-64](/linux/booting-linux-on-x86-64.md)