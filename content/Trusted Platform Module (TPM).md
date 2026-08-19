---
title: Trusted Platform Module (TPM)
date: 2026-05-25
tags:
  - security
  - hardware
share: true
---
TPM is a secure crypto processor on the motherboard. Used for 
- verifying that the boot process starts from trusted combination of hardware and software 
- storing disk encryption keys
- provides hardware random number generator [](Booting%20Linux%20on%20x86_64#KASLR%20(Kernel%20Address%20Space%20Layout%20Randomisation)%5D)
- secure generation of cryptographic keys

It creates a unforgeable hash key summary of hardware & software configuration. Sealed storage protects the private info by binding it to the platform with this hash key. This is used for DRM enforcement. [](Digitial%20Rights%20Management%20(DRM)%5D)

UEFI can use TPM to form root of trust. 

## Sources
- 
## Related
- [](Trusted%20Platform%20Module%20(TPM)%5D)