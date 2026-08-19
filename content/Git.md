---
title: Git
date: 2026-05-02
tags:
  - git
  - tooling
share: true
---
### Common git commands

- `git help <command>` : help for a command
- `git log --all --graph --decorate`: visualize history as DAG
- `git diff <revision> <filenam>`: diff between commit & cur file
- `git branch` : shows all branches
- `git branch <name>`: create new branch
- `git merge <revision>`: merges revision into current branch
- `git remote -v`: list remotes
- `git remote add <name> <url>`: add remote
- `git push <remote> <local branch>:<remote branch>` : send objs to remote & update remote refs
- `git fetch`: retrieve remote objs/refs
- `git pull`: same as `git fetch; git merge`
- `git reset HEAD <file>`: untrack a file
- `git config` : customize git your way
- `git add -p`: interactive staging
- `git rebase` : apply cur changes on new base
- `git rebase -i`: interactive rebase
- `git blame`: who made the change
- `git stash`: temp remove all mod to curr dir
- `git rev-parse HEAD` : shows current head

### Merge Strategies

If there're too many conflicts, and you just want to either accept our/their code, you can use flag `-X theirs` or `-X ours` with all git commands doing either merge/rebase.

| Currently on | Command           | Strategy      | Outcome                          |
| ------------ | ----------------- | ------------- | -------------------------------- |
| master       | git merge feature | **\-Xtheirs** | Keep changes from feature branch |
| master       | git merge feature | **\-Xours**   | keep changes from master branch  |
| feature      | git rebase master | **\-Xtheirs** | Keep changes from feature branch |
| feature      | git rebase master | **\-Xours**   | keep changes from master branch  |

### Git's data model as psuedo code

```
type blob = array<byte>

// name of file/dir => it's contents
type tree = map<string, tree | blob>

// commits can have multiple parents, and top level tree
type commit = struct {
  parent: array<commit>
  author: string
  message: string
  snapshot: tree
}

// all blob/tree/commit are unified as objs
type object = blob | tree | commit

// all objs are hashed and stored. key is the hash
objects = map<string, object>

def store(object):
  id = sha1(object)
  objects[id] = object

def load(id):
  return objects[id]

// human readable name (eg, master) => objects hash
references = map<string, string>

def update_reference(name, id):
  references[name] = id

def read_reference(name):
  return references[name]

def load_reference(name_or_id):
  if name_or_id in references:
    return load(references[name_or_id])
  else:
    return load(name_or_id)
```

- All folders are tree in git
- All files are blobs
- Commit is like snapshot of all files. They can be linked with multiple parents, which forms history.
- All blobs/tree/commits are represented as objects
- All objects are represented by SHA-1 hash of it's content, so it's easy to know when files change. 
- References then are human readable translation of hash of these objects (eg master/feature-fix-auth)
- `HEAD` is a reference of latest/current commit sha in the project
- All git objects except references are immutable (all that you do with destructive commands like `reset —hard` is just point to different references). Thus it's hard to lose any data in git.
- Git objects and references defines all the data inside git dir
- All git commands does is manipulate this DAG by adding objects, adding/updating references
- Use command: `git cat-file -p <hash>` to decode and print what git obj with hash contains
- Staged / Unstaged changes
	- When you make any change, git will show the change made, but this change is not yet tracked (ie, you can lose the changes)
	- To track the changes with git, you've add them by `git add <files>` . This stores all these changes in index (which is like a tree and keeps track of all changes added)
	- On commit, git uses this index to create current snapshot of project
- Three ways git merge
	- Checkout branch `b` from master, update a file and commit. Checkout back to master. What happens when you run `git merge b`
		- Git checks two commits of refs `master` & `b` and sees one is a parent of other, it just updates `master` to new commit & calls it a day
	- Checkout `b` , update a file `foo.txt`, while in a separate flow, master also updates file `bar.txt`
		- Git now sees two different commits, it traces back in history to a common commit. Checks what changed in these two new commits. Since changes are in separate files. It creates a new commit, with all changes, and sets the parent as the two commits.
	- Update same file as in master
		- Follow steps similar as above, but now it sees that commits in question have conflicting changes. It seeks developer assistance in resolving it, instead of being over smart.


### Oh shit git!
####  I did something terribly wrong, go back to what works

```bash
# everything you did with git in all branches
# copy HEAD@{index} where everything worked
git reflog

# phew!
git reset HEAD@{index}
```

#### I committed but forgot to make a small change/wrong commit message

```bash
git add .
git commit --amend --no-edit
```

#### Accidentally committed to master, when it should've been to new branch

```bash
git branch new-branch

# removes last commit from master
git reset HEAD~ --hard

# this branch still contains the commit though!
git checkout new-branch
```

#### Accidentally committed to wrong branch

```bash
git checkout correct-branch

# get the last commit to master
git cherry-pick master

git checkout master
git reset HEAD~ --hard

```

#### Undo a commit from like 5 commits ago

```bash
# find the commit
git log

git revert <hash>
```

#### Undo my changes to a file

```bash
# find hash before the file was changed
git log

# set's old version in index
git checkout <hash> -- <path/to/file>

git commit -m "you can do this smartly too"
```


## Sources
- https://missing.csail.mit.edu/2026/version-control/
## Related
- [](%5D)