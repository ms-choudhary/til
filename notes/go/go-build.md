# Go build

### Cross compilation

```
env GOOS=target-OS GOARCH=target-architecture go build package-import-path
```

where target-os can be: `linux, darwin, android, windows, freebsd, netbsd, openbsd, dragonfly, plan9`  
where target-architecture can be: `arm, arm64, amd64`

### Static build

Using static build, go skips linking to libc/musl libraries. Instead implements it's own library calling syscall directly. 

```
CGO_ENABLED=0 go build -a -ldflags '-extldflags "-static"' .
```

### Go always builds binaries with versioning

If you run go build from a git repository, it versions the binary by default. 

```
$ go version -m gmail2gullak | grep vcs
        build   vcs=git
        build   vcs.revision=a952a27dab46dfe460bb209a9b39a1bae6b15ffd
        build   vcs.time=2026-04-24T12:08:34Z
        
$ go version gmail2gullak
gmail2gullak: go1.25.0
```

This also prints which go toolchain was used to build the binary. 

## Sources
- 
## Questions
- 
## Related
- [go-compilation-tools](/notes/go/go-compilation-tools.md)
