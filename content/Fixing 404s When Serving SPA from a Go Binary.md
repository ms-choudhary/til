---
title: Fixing 404s When Serving SPA from a Go Binary
updated: 2026-03-09 11:53:18Z
date: 2026-03-07 06:07:12Z
tags:
  - ui
  - golang
share: true
---
This is a sample go code I was using to host frontend UI directly from golang:

```
//go:embed ui/dist/*
var frontendFS embed.FS

func main() {
	distFS, err := fs.Sub(frontendFS, "ui/dist")
	if err != nil {
		log.Fatal(err)
	}

	frontendHandler := http.FileServer(http.FS(distFS))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		frontendHandler.ServeHTTP(w, r)
	})

	log.Printf("listening on: localhost:9876")
	log.Fatal(http.ListenAndServe(":9876", nil))
}
```

For the frontend, I was using Vue.js (I don't have much experience in frontend), which compiles everything after `npm run build` into `ui/dist`. 

We then embed `ui/dist/` directory in go binary. And finally, we use `http.FileServer`  to serve files from the go server, which defaults to serving `ui/dist/index.html`. 

I wanted the Vue.js framework to handle `/custom` URL path, to show a different page. I had implemented UI changes, and they were working fine when tested separately. But when accessing them via go server, I was getting `404 page not found`. 

After little bit of fiddling, I figured out it was because `http.FileServer` was trying to serve a file called `custom` and when it couldn't find, it returned 404. 

The fix was to serve `index.html` for any path where file doesn't exist and let Vue handle the routing:
```

	  indexHTML, err := fs.ReadFile(distFS, "index.html")
	  if err != nil {
		  log.Fatal(err)
	  }
	  
    // serve index.html for any path that does not exists
    // and let vue handle the routing
    _, err = distFS.Open(path)
    if err != nil {
			w.Header().Set("Content-Type", "text/html; charset=utf-8")
			if _, err := w.Write(indexHTML); err != nil {
				log.Printf("failed to write index.html fallback: %v", err)
			}
			return
    }

```

## Questions
- 
## Related
- [](Fixing%20404s%20When%20Serving%20SPA%20from%20a%20Go%20Binary%5D)