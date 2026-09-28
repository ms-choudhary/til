# git worktree 

Git worktree allow you to create multiple work dir from the same repo, each checked out to different branch. 

For eg, if you're working on a feature and want to check something on main, traditionally you had to do:
```
git add .
git commit -m 'changes'

git checkout main
# finally checkout feature branch to continue working 
git checkout -
```

With worktrees:
```
git worktree add ../test-main main
cd ../test-main
```

This creates a new dir at same level of the repo with main branch checked out. So basically instead of one working dir and switching between branches, you create multiple working dirs each with different branch. 

Each of these copies share the same git history. 
### Worktree add

```
git worktree add <path> <branch>
```
### Create new branch in worktree

```
git worktree add -b feature-2 ../test-feature2
```
### List

```
git worktree list
```


