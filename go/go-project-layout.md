# Go project layout

### Project Layout
Code is structured in golang using **files, packages & modules**. Each new dir indicates a new package.  

Only create a new package if you see demonstrable need for it. It's okay for files to be longer. Focus should be on reusability. Package should be standalone, isolated and should enforce boundaries with other code. 

#### Simple
```
├── main.go
├── foo.go
├── bar.go
├── go.mod
└── README.md
```
#### Small with supporting packages
```
├── internal
│   └── foo
│       └── foo.go
├── main.go
├── bar.go
├── go.mod
└── README.md
```

#### Large 
Consists of lots of non go assets (eg templates, database migration etc). Also multiple binaries like (server, client etc). 

```
├── cmd
│   └── foo
│       ├── main.go
│       └── bar.go
├── internal
│   └── baz
│       └── baz.go
├── go.mod
├── Makefile
└── README.md
```


## Sources
- https://www.alexedwards.net/blog/11-tips-for-structuring-your-go-projects
## Related
- [go-language](/go/go-language.md)