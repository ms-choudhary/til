# Shell Commands

**Source**: 

### Reverse a file

```
tac
or
tail -r
```

### Show file with linenumber

```
cat -n filename

less -N filename or type -N in less window

vim file => :set number
```


### Match/unmatch patterns from file
- Find entries which are present in all but missing in processed to left_over (does not require sorting):

```
grep -vxFf processed all > left_over

-v = invert search
-x = match whole lines
-F = treat patterns literally (no regex)
```

### How to create multiple incremented nos directory
```
mkdir -p pre{00..14}

mkdir -p pre{00,12,13}
```

### Keyboard Shortcuts

`CTRL-A` = go to the begining of the line  
`CTRL-E` = go to the end of the line  
`CTRL-U` = delete everything till begining  
`CTRL-K` = delete everyting till end

### Job control
- disown - removes the job from list of running jobs, so it doesn't get killed when you exit the terminal, **ensure it doesn't write into terminal window**
```
some_long_command > /tmp/log 2>&1
CTRL-Z
bg
disown %1
```
- `nohup command` - same as above

### Readlink

Get path to actual file to which a symlink points

```
readlink -f path
```

## Questions
- 
## Related
- [terminal](/notes/linux/terminal.md)
- [vim](/notes/shell/vim.md)

