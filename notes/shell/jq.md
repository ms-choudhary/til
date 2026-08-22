# jq command

### Decoding JWT using jq
JWT token can be decoded using jq:
```
jwt-decode () {
        jq -R 'split(".") |.[0:2] | map(@base64d) | map(fromjson)' <<< $1
}
```
- `--raw-input/-R` = don't parse input as json instead pass as string
- map(x), map_values(x)
       For any filter x, map(x) will run that filter for each element of the input array, and return the outputs in a new array.
- `@base64d` = base64 decode
- Convert to/from JSON
       The  tojson  and  fromjson builtins dump values as JSON texts or parse JSON texts into values, respectively.

### Print fields as string

```
 $ docker image inspect miniflux/miniflux | jq '.[] | "\(.Os)\/\(.Architecture)"'
"linux/arm64"
```

- has string in quotes
- escape special chars



## Sources
- 
## Questions
- 
## Related
- [oidc](/security/oidc.md)
