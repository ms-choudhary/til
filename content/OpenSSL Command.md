---
title: OpenSSL
date: 2026-03-31
tags:
  - security
  - tooling
share: true
---

**Source**: 

### Inspect certificate

```
openssl x509 -in input.crt -noout -text
```

### Inspect certificate from URL

```
echo | openssl s_client -connect burrow.test.indexexchange.com:443 | openssl x509 -noout -text
```

### Remove passphrase from a private key

```
openssl ec -in input.key -out output.key
```

## Questions
- 
## Related
- [](OpenSSL%20Command%5D)
- [](OpenSSL%20Command%5D)
- [](OpenSSL%20Command%5D)
