---
title: Data encoding
date: 2026-05-02
tags:
  - storage
  - security
share: true
---
## base32 

base32 encodes binary data into set of ASCII chars, 26 letters (A-Z) & 2-7 numerals. 

It takes 5 bit of input and converts it into a char. Since data is generally represented in 8-bits byte, it processes a 5 byte input chunk (40 bit) and generates a 8 chars of output. Padding '=' is added at the end if input is not a multiple of 5. Padding is extra, and data can be decoded (although with errors) without it. 

### Use cases
- TOTP
- case insensitive systems like dns, filesystem etc
## base64 

base64 encodes binary data into 64 ASCII chars:
- A-Z
- a-z
- 0-9
- + / (2 special chars)
- = (padding at the end)

Processes a 6 bit input to one char. Takes 3 bytes (24 bit) to produce 4 chars. If input is not a multiple of 3 bytes, padding is added at the end. 


### Use cases

- converts binary data into representable text
	- email attachments 
	- image css in html 


## URL encoding

URL encoding replaces unsafe chars with % followed by 2 digit hex value. Almost all chars are unsafe except few. 

## Sources
- 
## Related
- [](HTTP#URL%5D)