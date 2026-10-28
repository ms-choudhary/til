# Nginx

### Template Envsubst

`nginx:alpine` sources `/docker-entrypoint.d/20-envsubst-on-templates.sh` which allows you substitute environment variables in the template dir at runtime. Example,

```
services:
  marquee:
    image: nginx:alpine
    container_name: marquee
    restart: unless-stopped
    environment:
      - TMDB_API_KEY=[secret]
      - NGINX_ENVSUBST_FILTER=^TMDB_
      - NGINX_ENVSUBST_OUTPUT_DIR=/usr/share/nginx/html
    volumes:
      - ./site.html:/etc/nginx/templates/index.html.template:ro
      - ./nginx-default.conf:/etc/nginx/conf.d/default.conf:ro
```