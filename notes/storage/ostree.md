# ostree

ostree is git for filesystems. It enables versioning, distribution & atomic deployment of linux systems. 

It stores complete system snapshot, making updates & rollbacks easier. 

Based on composefs, relies on EROFS (Enhanced Read Only Filesystem), which guarantees against data corruption, and natively performs data deduplication & LZ4 compression. 

Data is in `/sysroot/ostree/repo/objects`.
Similar to git, allows creating commits, versions & switch between them. 

Only /var is mutable, other mutable dirs are symlinked to var. /etc is special overlay, it intelligently merges new changes with old. #question explore this more. 

It uses rpm-ostree package manager. #question what can it do/not do compared to dnf?

Which creates new commits but changes are not affected until reboot. 

Can use `rpm-ostree rollback` to rollback to previous commit. 

## Sources
- [https://lwn.net/Articles/581811/](https://lwn.net/Articles/581811/)
- [https://blog.verbum.org/2014/01/21/ostree-in-action-rpm-ostree-and-switching-trees/](https://blog.verbum.org/2014/01/21/ostree-in-action-rpm-ostree-and-switching-trees/)
- [https://github.com/coreos/rpm-ostree/blob/main/docs/background.md](https://github.com/coreos/rpm-ostree/blob/main/docs/background.md)
## Related
- [[]]