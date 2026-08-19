# Trusted Platform Module (TPM)

TPM is a secure crypto processor on the motherboard. Used for 
- verifying that the boot process starts from trusted combination of hardware and software 
- storing disk encryption keys
- provides hardware random number generator [[Learn/linux/booting-linux-on-x86-64#KASLR (Kernel Address Space Layout Randomisation)]]
- secure generation of cryptographic keys

It creates a unforgeable hash key summary of hardware & software configuration. Sealed storage protects the private info by binding it to the platform with this hash key. This is used for DRM enforcement. [[Learn/security/drm]]

UEFI can use TPM to form root of trust. 

## Sources
- 
## Related
- [booting-linux-on-x86-64](/linux/booting-linux-on-x86-64.md)