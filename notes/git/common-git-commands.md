# Common git commands

### List Remotes

```
git remote -v
```

### Add remote

```
git remote add <name> <url>
```
### Show current head

Used in scripting:

```
git rev-parse HEAD
```

### Visualize history as DAG

```
git log --all --graph --decorate
```

### Interactive staging

```
git add -p .
```

Note: this doesn't consider untracked changes (new files not added yet). To add them:

```
git add -N .
```

`-N` = `--intent-to-add`


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