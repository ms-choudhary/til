---
title: Certificate management using step-cli
updated: 2025-09-29 17:31:16Z
date: 2026-03-31
tags:
  - security
  - tooling
  - 
share: true
---


**Source**: 
### Install step-cli

https://smallstep.com/docs/step-cli/installation/

### Create a new root CA, then create a new certificate and private key using step cli

```
$ step certificate create root-ca root-ca.crt root-ca.key --profile root-ca

$ step certificate create foo foo.crt foo.key --profile leaf \
            --ca root-ca.crt --ca-key root-ca.key --san 10.230.32.1 --san 10.230.32.2
```

## Questions
- 
## Related
- [](Certificate%20management%20using%20step-cli%5D)
- [](Certificate%20management%20using%20step-cli%5D)
- [](Certificate%20management%20using%20step-cli%5D)
