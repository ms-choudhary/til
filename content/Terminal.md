---
title: Terminal
date: 2026-04-08
tags:
  - linux
share: true
---
**Source**: 

Terminal is a pair master and slave devices. Slave devices are like dumb clients without any intelligence just relaying what user types to the server and showing back the response. 

Now when you type text on the terminal, it's relayed back to master device, which gives the information to program running. There're escape sequences to display text in bold or color, cursor movement etc. When you type `Ctrl-C` or `Ctrl-Z` it sends a ascii signal `\x03` and `26`. This is intercepted by kernel (and not userspace program like shell), and it sends `SIGINT` signal to process group in the terminal. 

When the master device starts, it makes this sys call:

```
syscall.Syscall(
    syscall.SYS_IOCTL,
    tty.Fd(),
    syscall.TIOCSWINSZ,
    uintptr(unsafe.Pointer(&resizeMessage)),
)
```

this calls the ioctl system call. To check terminal parameters, you can type:

```
stty -a

or

tputs cols # for columns 
```

when you change the window size of the terminal, kernel sends a signal `SIGWINCH` which resets the stty cols etc. The side effect of this not being correctly set will result in overwriting of text of same line and not changing to next line on inputting long text in the terminal. 

## Questions
- 
## Related
- [](Command%20Line%20Foo#Job%20control%5D)
- [](Command%20Line%20Foo#Keyboard%20Shortcuts%5D)