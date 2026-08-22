# Inspect VM filesystem

**Source**: https://linux.die.net/man/1/guestfish

To inspect files inside VM disk (qcow2, img or other kinds), install guestfish:

```
apt install libguestfs-tools
```

```
guestfish 
> add-ro debian.qcow2
> run
> help mount-ro
```

Type help gives you what you should do next. You can copy files to host via `copy-out /file/in/qcow2 /host/dir/`

## Questions
- There's a way to install os by using qcow2 image (without running the installer). How does that work? #question 
## Related
- [dd](/notes/storage/dd.md)
- [taking-vm-snapshots-in-utm](/notes/utm/taking-vm-snapshots-in-utm.md)
