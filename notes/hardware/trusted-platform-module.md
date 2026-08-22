# Trusted Platform Module (TPM)

TPM is a secure crypto processor on the motherboard. Used for 
- verifying that the boot process starts from trusted combination of hardware and software 
- storing disk encryption keys
- provides hardware random number generator [KASLR (Kernel Address Space Layout Randomisation)](/notes/linux/booting-linux-on-x86-64.md#KASLR%20(Kernel%20Address%20Space%20Layout%20Randomisation))
- secure generation of cryptographic keys

It creates a unforgeable hash key summary of hardware & software configuration. Sealed storage protects the private info by binding it to the platform with this hash key. This is used for DRM enforcement. [drm](/notes/security/drm.md)

UEFI can use TPM to form root of trust. 

## Sources
- 
## Related
- [booting-linux-on-x86-64](/notes/linux/booting-linux-on-x86-64.md)