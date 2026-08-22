# OpenSSL Command

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
- [certificate-management-using-step-cli](/certificates/certificate-management-using-step-cli.md)
- [set-time-on-linux](/shell/set-time-on-linux.md)
- [pki-certificates](/certificates/pki-certificates.md)