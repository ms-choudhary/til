---
title: Macos
date: 2024-11-13 04:59:36Z
tags:
  - macos
  - 
share: true
---
### Keyboard

- `Settings -> Keyboard -> Key repeat rate` controls at what speed when pressing a key the input is sent, if you make it high, cursor will move faster when you press let's say down key etc. 

### Safe mode boot

- To boot in safe mode, shutdown the mac
- Keep pressing the power button till, it loads startup option
- Select the drive and continue


### Clear DNS cache

```
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```
### Directories

- `~/Library/Caches` all system wide caches for applications
- `~/Library/Preferences` plist files used for storing configuration, preferences etc. 

### Type degree (°) symbol

Option + Shift + 8 => °

### Rebuild spotlight index

- For a specific dir, for eg Applications:
	- Setting -> Spotlight -> Search Privacy 
		- Add and remove the directory
- For all dirs
```
	sudo mdutil -Eai off
	sudo mdutil -Eai on
```

## Sources
- 
## Questions
- 
## Related
- [](%5D)
