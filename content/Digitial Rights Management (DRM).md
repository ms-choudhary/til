---
title: Digitial Rights Management (DRM)
date: 2026-05-26
tags:
  - security
share: true
---
DRM takes control of the digital content from the users to a software program. It helps prevent unauthorised sharing or modification of IP. Used by services like Netflix, PrimeVideo etc. 

Some popular DRM systems include, also known as, Content Decryption Module (CDM):
- Widevine (Google) - included with all browsers
- Fair Play (Apple) - Safari, iOS - perhaps why the player is different
- Playready (MS)

Typical flow involves, a movie or stream is encrypted. When you hit play, device requests the decryption key. The request includes, user credentials, device info (used for selecting decryption layer) and DRM type (widevine etc). Companies package content in multiple DRMs and serve the right one based on what the browser supports. If everything checks out, it sends a decryption key. Video is only decrypted in real time. 

W3C Encrypted Media Extensions (EME) spec is the browser API which all browsers implement. They might use different CDM underneath (For eg apple uses Fair play, chrome/android - widevine etc). 
### L1 - Hardware level security

Decryption & processing happens entirely with TEE (Trusted Execution Environment). Requires device support. For eg, netflix allows playing 4k only on devices which support L1. 

### L2 - Mix of hardware and software

Uses some features of hardware and software. Limited to 1080p. 

### L3 - Software only

Decryption happens in memory (RAM). Handled at OS/Browser level. Susceptible to theft from RAM by compromised kernel or privildged process. Limited to 480p to 720p resolution for the same reason. All decrypted videos have a invisible watermark, with user info, useful to find the culprit if a video is copied and leaked.  


## Sources
- 
## Related
- [](Trusted%20Platform%20Module%20(TPM)%5D)


