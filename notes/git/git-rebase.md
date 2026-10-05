# Git Rebase

### Interactive rebase

Used for squashing commits:

```
git rebase -i origin main
```

```
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
```