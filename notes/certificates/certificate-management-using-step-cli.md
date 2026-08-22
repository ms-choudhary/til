# Certificate management using step-cli

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
- [openssl](/notes/certificates/openssl.md)
- [set-time-on-linux](/notes/shell/set-time-on-linux.md)
- [pki-certificates](/notes/certificates/pki-certificates.md)