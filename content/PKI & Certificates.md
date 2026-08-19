---
title: PKI & Certificates
date: 2026-05-20
tags:
  - http
  - security
share: true
---
### Terminology
- **Entity**: anything that exists! your computer, your code
- **Identity**: attributes which define an entity
- **Claim**: Entities can claim they've certain name, Authentication, then, is the process of asserting that claim
- **Subscriber**: Server which participates in PKI, subject of the certificate
- **Issuer or Certificate Authority (CA)**: Entity that issues certificates to subscribers.
- **Relying Party (your browser):** Entity which uses certificates
### Symmetric cryptography
- Uses one-way hash functions(eg HMAC), which accepts message & pre-shared secret key as input and generate signature. Client can then ensure message integrity following same steps
### Asymmetric cryptography / Public key cryptography
- Uses public/private keys to
	- either encrypt data with public key. This can then only be decrypted using private key
	- sign some data with private key. Anyone who has public key can verify this signature
### Certificates
- In simple terms: "bind names to public key"
- Allows computer to see who it's communicating with
- In other words, it's a data structure of public key and name, which is signed by *issuer*
- But what does it actually contain?
	- Public key
	- Name (Subject Alternative Name - SAN)
	- Issued at, expires at dates
	- Crptographic signature
		
		![](PKI & Certificates)
		
	
- SSH has it's own format of certificate
	- when you edit `~/.ssh/authorized_keys` you configure a way of certificate less way of PKI to bind public key to name
- X.509
	- The kind of certificate which browsers understand and use for HTTPS or almost always used for internal PKI setup
	- Originally built for telcos to build global telephone dir in 1980s. Still reeks of that design. Most fields are out dated, hence not required to be filled
	- Builds on ASN (Abstract Syntax Notation) for defining types, similar to JSON
	- Most common encoding, DER (Distinguished Encoding Rules) consists of binary data, packaged as PEM files (base64 payload sandwiched between headers)
	
	```bash
	-----BEGIN CERTIFICATE-----
	MIIBwzCCAWqgAwIBAgIRAIi5QRl9kz1wb+SUP20gB1kwCgYIKoZIzj0EAwIwGzEZ
	MBcGA1UEAxMQTDVkIFRlc3QgUm9vdCBDQTAeFw0xODExMDYyMjA0MDNaFw0yODEx
	MDMyMjA0MDNaMCMxITAfBgNVBAMTGEw1ZCBUZXN0IEludGVybWVkaWF0ZSBDQTBZ
	MBMGByqGSM49AgEGCCqGSM49AwEHA0IABAST8h+JftPkPocZyuZ5CVuPUk3vUtgo
	cgRbkYk7Ong7ey/fM5fJdRNdeW6SouV5h3nF9JvYKEXuoymSNjGbKomjgYYwgYMw
	DgYDVR0PAQH/BAQDAgGmMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAS
	BgNVHRMBAf8ECDAGAQH/AgEAMB0GA1UdDgQWBBRc+LHppFk8sflIpm/XKpbNMwx3
	SDAfBgNVHSMEGDAWgBTirEpzC7/gexnnz7ozjWKd71lz5DAKBggqhkjOPQQDAgNH
	ADBEAiAejDEfua7dud78lxWe9eYxYcM93mlUMFIzbWlOJzg+rgIgcdtU9wIKmn5q
	FU3iOiRP5VyLNmrsQD3/ItjUN1f1ouY=
	-----END CERTIFICATE-----
	```
	
	- Sometimes certificate is wrapped fancier packaging, which can contain multiple certificates (bundle). These are part of standards called **PKCS**
### Public Key Infrastructure (PKI)
- umbrella term used for store, use, verify, revoke of certificates & keys. as vague as "database infrastructure"
- Web/Internet PKI
	- works by default with browsers and TLS
- Internal PKI
	- Why can't we use web PKI for internal workloads as well?
		- to have better control on certificate attributes (like issue/expiry date)
		- there might be rate limit or availability issues with CA
### Root certificates
- Relying parties has pre-installed list of root certificates
- Root certificate is self signed `Mike says Mike is blah blah blah`
- Root CAs are regulated via various programs (like apple root certificate, microsoft root certificate, mozilla's root certificate)
- OS's are shipped with it's own trust stores (these are what are used when you use `curl` or some programming library for TLS)
### Intermediate certificates
- CAs can be online or offline, based on whether they provide an APIs to issue certificates
- Root CAs are always offline
- Root private key is used infrequently to sign intermediate certificates (which are easier to revoke/rotate)
- Intermediate certificates are validated in same steps as leaf certificate
- When certificate are exchanged in TLS (Web PKI), it's passed as bundle (leaf certificate, is signed by layers of intermediate cert, which is signed by root cert)
- When you're setting up proxy (like nginx) you need to specify this bundle instead of leaf certificate
- These bundles are encoded as simple line separated PEM objects (eg)

![](PKI & Certificates)

- Relying parties then verify all certificates in the bundle (certificate path validation)
### Certificate management
#### Naming
- Historically, DNs was used to name the subject of certificate (*subscriber*). This was deprecated, and DN is now optional.
- SAN (Subject Alternative Name) is now used for subject. 4 sort of SANs are in common use: DNS, Email address, IP address & URI
- SAN can have multiple names (`smallstep.com`, [`www.smallstep.com`](http://www.smallstep.com), `*.smallstep.com` )
#### Generating key pairs
- If using RSA, use at least 2048 bits
- If using ECDSA, P-256 curve is probably best (`secp256kl` or `prime256v1` in openssl) eg in openssl:

```bash
openssl ecparam -name prime256v1 -genkey -out k.prv
openssl ec -in es256.key -pubout -out k.pub
```
	
#### Issuance
- Next step after name & key pair is to obtain leaf certificate from CA
- CA will check two things:
	- public key which will be part of cert, is subscriber's public key, done by Certificate signing request (CSR)
	- name in the cert, is subscriber's name, done by Identity proofing/registration
- Certificate signing request (CSR)
	- Like cert, contains public key, name & signature. It's self signed by subscriber's private key
- Identity proofing
	- Kinds of certificates for Web PKI
		- Domain Validation (DV)
			- DV certificates bind DNS name, issued based on proof of control over domain name
			- Traditionally it sends a confirm email to administrative contacts list in WHOIS records
			- ACME protocol (developed by Let's Encrypt) automates this process. It issues a challenge that subscriber must complete to prove control of domain (common challenge include serving random number at given URL(http challenge) or placing random number in DNS TXT record(dns challenge)
		- Organization Validation (OV), Extended Validation (EV)
			- These build on DV they bind not just domain name but also legal entity (organization) that controls it.
			- OV is deprecated in favour of EV
			- EV process takes long time (days or week), can include physical application
			
			![](PKI & Certificates)
				
#### Expiry
- New certificate should be replaced with the expiry cert
- For internal PKI, you should use shorter expiry times
- For internal PKI, you can automate expiry by requesting new cert (with longer expiry) by giving older cert
#### Revocation
- There are provisions to revoke a compromised certificate, but acceptance by relying parties are not uniform
- To revoke you can add in Certificate Revocation List (CRLs) or Online Certificate Signing Protocol (OCSP)



## Sources
- https://smallstep.com/blog/everything-pki/
## Related
- [](PKI%20&%20Certificates%5D)
- [](PKI%20&%20Certificates%5D)
- [](Data%20encoding#base64%5D)
- [](PKI%20&%20Certificates%5D)