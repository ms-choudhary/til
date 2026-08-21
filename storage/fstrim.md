# fstrim

Discard unused blocks on a mounted filesystems. Useful for reducing the image size on a VM. Must be supported by the device. Check:

```
$ lsblk --discard/-D
NAME   DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
vda           0      512B      64G         0
├─vda1        0      512B      64G         0
├─vda2        0      512B      64G         0
└─vda3        0      512B      64G         0
```

to check discarding capabilities of each block device. 

DISC-ALN: Disk alignment
DISC-GRAN: Disk granularity, smallest chunk which can be discarded
DISC-MAX: Largest amount which can be discarded in a single request

If you're using packer with qemu/kvm, use newer devices `q35` over `pc` (outdated intel), which might not support discard.  

```
fstrim /path/to/mount
```

