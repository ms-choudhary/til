# TOTP

TOTP is Time based One Time Password. 

Server generates a base32 secret (without padding '='), and shares to client via QR. QR code encodes a link of format: `otpauth://totp/github:john@example.com?secret=xyz&issuer=github&algo=sha1`. Client stores the secret. 

The other thing shared between server & client is time. 30s interval window is selected, so it's easy for user to add the code, and it nullifies millisecond and microsecond differences between client and server's clock.

```
currTimeInS := currentTimestamp in unix secs
counter := currTimeInS/30 

code := hash.Sha1(secret, counter) // generates a 20-byte hash

opt := truncateTo6Digits(code)

// dynamic truncate
Last hex for eg 0x5a => integer, eg 10 => get 4 bytes from offset => integer => truncate
```

Client and server performs the same computation over 30s intervals, and should match for success. 


## Sources
- https://www.youtube.com/watch?v=HFu3CUtrOQ8
## Related
- [base32](/notes/security/data-encoding.md#base32)
- [pki-certificates](/notes/certificates/pki-certificates.md)