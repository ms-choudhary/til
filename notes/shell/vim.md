# Vim

**Source**: 

### Write as sudo trick

```
:w !sudo tee %
```

% = current file name in execution command context (in substitution context it means entire file buffer)

### No paste

To ignore indenting while pasting text in vim
```
:set paste
:set nopaste
```

### Open at line number

```
vim +13 /root/.ssh/known_hosts
```

## Questions
- 
## Related
- [Show file with linenumber](/notes/shell/shell-commands.md#Show%20file%20with%20linenumber)
