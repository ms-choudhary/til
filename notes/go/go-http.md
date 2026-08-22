# Go HTTP

## Mux

```
func main() {
    mux := http.NewServeMux()

    mux.HandleFunc("GET /posts",          listPosts)
    mux.HandleFunc("POST /posts",         createPost)
    mux.HandleFunc("GET /posts/{id}",     getPost)
    mux.HandleFunc("PUT /posts/{id}",     updatePost)
    mux.HandleFunc("DELETE /posts/{id}",  deletePost)

    http.ListenAndServe(":8080", mux)
}
```

### Path values

```
mux.HandleFunc("GET /users/{id}", func(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id")  // new in 1.22
    fmt.Fprintf(w, "User ID: %s", id)
})
```
## HTTP Middleware
### Pattern
```
func exampleMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Your middleware logic goes here...
		next.ServeHTTP(w, r)
	})
}

func fooHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("foo"))
}

func main() {
	mux := http.NewServeMux()
	mux.Handle("/foo", exampleMiddleware(http.HandleFunc(fooHandler)))
	
	log.Fatal(http.ListenAndServe(":3000", mux))
}
```

To add middleware for all routes, add it on http.ServeMux() (since it implements http.Handler interface). 

```
log.Fatal(http.ListenAndServe(":3000", myMiddleware(mux)))
```

### Chain

```
type chain []func(http.Handler) http.Handler

func (c chain) thenFunc(h http.HandlerFunc) http.Handler {
    return c.then(h)
}

func (c chain) then(h http.Handler) http.Handler {
    for _, mw := range slices.Backward(c) {
        h = mw(h)
    }
    return h
}
```

Usage:
```
mux := http.NewServeMux()

// Create a base middleware chain. 
baseChain := chain{requestID, logRequest}

// Extend the base chain with auth middleware for admin-only routes.
adminChain := append(baseChain, authenticateUser, requireAdminUser)

mux.Handle("GET /static/", spaHandler(http.FileServerFS(ui.Files)))

mux.Handle("GET /", baseChain.thenFunc(home))
mux.Handle("GET /article/{id}", baseChain.thenFunc(showArticle))

mux.Handle("GET /admin", adminChain.thenFunc(showAdminDashboard))
```
### Use cases
- Check if user is authenticated
- Check for headers like `Content-Type`
- Implement rate limit logic
- Add http headers in response
- Log request & response automatically using `log/slog`
## Sources
- https://www.alexedwards.net/blog/making-and-using-middleware
- https://www.alexedwards.net/blog/organize-your-go-middleware-without-dependencies
## Related
- [handling-spa-go](/notes/go/handling-spa-go.md)