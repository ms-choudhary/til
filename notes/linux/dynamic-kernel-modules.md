# Dynamic kernel modules
### Dynamic Kernel Module Support (DKMS)

DKMS allows building kernel modules whose source reside outside the kernel source tree. 

It auto recompiles all DKMS modules if a new kernel version is installed. 

This allows drives to continue working after kernel upgrade. Also allows installation of new drivers on existing system without any need for manual compilation. 

Supports rpm & deb packages out of the box. 

### Akmods (fedora)

kmod package contains precompiled modules for a kernel version. It doesn't work if the kernel version is different. 

Akmods allows rebuilding the modules for a different kernel. 

`akmodsd` daemon starts at the init, and checks if all kmods are present and compatible. It auto rebuilds missing/incompatible kmods, and installs into the running kernel. 


## Sources
- https://rpmfusion.org/Packaging/KernelModules/Akmods
- https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support
## Related
- [package-management](/notes/linux/package-management.md)