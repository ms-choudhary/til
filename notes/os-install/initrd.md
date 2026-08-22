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
- [cobbler](/notes/os-install/cobbler.md)
- [anaconda](/notes/os-install/anaconda.md)
- [inspect-vm-filesystem](/notes/virtualization/inspect-vm-filesystem.md)
- [dd](/notes/storage/dd.md)
- [grub](/notes/os-install/grub.md)
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)