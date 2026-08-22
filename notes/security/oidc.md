# Openid Connect (OIDC)

**Source**: https://dexidp.io/docs/openid-connect/

### Oauth2

Popular single sign on workflow, for eg with google:
- You login to application via google
- It is redirected to google login form
- You authenticate to google using your google creds
- You're redirected back to application with token, and are now authenticated to the application
### ID Tokens

Tokens provided in oauth2 are generally opaque to client and provider specific. OIDC standardises the flow including the tokens as Json Web Token (JWT). Token consists of well known fields: header, payload and signature (of the first two fields). 

```
[
   # header
  {
    "alg": "RS256",
    "kid": "9151f75528677cd0c33a635340053dfd77f8d13f"
  },
  # payload
  {
    "iss": "https://ixdev.mschoudhary.site/",
    "sub": "CgcxODQxMTIzEgZnaXRodWI",
    "aud": "kubernetes",
    "exp": 1775038239,
    "iat": 1774951839,
    "jti": "37d5ef0e-ba82-4824-9c1c-58c06bf5fca9",
    "nonce": "gfInD0FryxFUqfzmdFRd8JKfe9j2U8XPWkxQMLEyFmI",
    "auth_time": 1774951838,
    "at_hash": "Kax3OY7scPt7souT8r1KSg",
    "c_hash": "bF1DxR19BltzjxvUjELSUg",
    "email": "ms.choudhary2000@gmail.com",
    "email_verified": true,
    "name": "Mohit Choudhary",
    "preferred_username": "ms-choudhary"
  }
  
  #signature
  ....
]
```

- iss - the oidc server who issued this token
- sub - unique end user id
- aud - client for which this token was issued for

While authenticating clients can request extra scopes (all supported scopes are listed in discovery endpoint), and server provides the same as additional claims (email, profile etc) in the token. 
### Discovery

All OIDC implement a well known discovery url: `/.well-known/openid-configuration`, which shows all configurations of OIDC server. 

Other endpoints:
- `authorization_endpoint` used for authenticating
- `jwks_uri` provides public keys of the server, used to verify the signature. 
- `claims_supported`
- `scope_supported`
### Flow

- Connect to `authorization_endpoint` (in wellknown configuration endpoint)
- Authenticate with the identity provider (like google, github, jumpcloud etc)
- You're redirected back to the redirect_url configured in IDP. 

### Tokens

In response, you get three tokens:
- **ID token**, this is the identity token used to authenticate the user. (Like government id in concert, you show this just once)
- **Access token**, this is the token used to interact with the apis. (Like wrist band in concert). This is has minimal fields. 
- **Refresh token** (optional), token used to refresh all of these tokens if they expire etc. 

#### Refresh Token

Generally in OIDC, you don't get refresh token by default. You've to request an additional scope `offline_access` when making the first request, thereby you authorising the client app to refresh tokens on your behalf. IDP should support this scope. 

You can exchange a refresh token with new valid tokens. For security reasons, any refresh token can only be used once, it returns all new tokens (id, access & refresh).

This facilitates functionalities, like relogin after 24 hours of inactivity. For eg, if client is active, it can refresh tokens automatically. However, if client is inactive and refresh token expires, you've to reauthenticate again. 
### Scopes & Claims

**Scope** is what you request when you initiate the flow. 
For eg, I'm interested in these category of information. 
**Claims** is what you receive

Scope unlocks claims. Some standard scopes and claims:
- openid => sub, iss, aud, exp, iat
- email => email, email_verified
- profile => name, given_name, family_name etc
- groups => groups

All supported scopes are listed in discovery endpoint. You can implement custom scopes as well, and introduce custom claims, specific to your app.  

## Questions
- 
## Related
- [Decoding JWT using jq](/notes/shell/jq.md#Decoding%20JWT%20using%20jq)
- [query-ldap-schema](/notes/security/query-ldap-schema.md)
