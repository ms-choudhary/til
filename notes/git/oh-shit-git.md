# Oh shit git!
### I committed but forgot to make a small change/wrong commit message

```bash
git add .
git commit --amend --no-edit
```

### Accidentally committed to master, when it should've been to new branch

```bash
git branch new-branch

# removes last commit from master
git reset HEAD~ --hard

# this branch still contains the commit though!
git checkout new-branch
```

### Accidentally committed to wrong branch

```bash
git checkout correct-branch

# get the last commit to master
git cherry-pick master

git checkout master
git reset HEAD~ --hard

```

### Undo a commit from like 5 commits ago

```bash
# find the commit
git log

git revert <hash>
```

### Undo my changes to a file

```bash
# find hash before the file was changed
git log

# set's old version in index
git checkout <hash> -- <path/to/file>

git commit -m "you can do this smartly too"
```



## Related
- 