---
title: Golang
date: 2024-09-24 09:32:10Z
tags:
  - golang
share: true
---
## Array, Slices

Source: https://go.dev/blog/slices
- Array is the building block of contingous items, contains size as part of it's definition. eg `var buffer [256]byte`. Arrays are always fixed size.
- Slice is a datastructure which describes a contiguous section of array: `var slice []byte = buffer[100:150]`. Behind the scenes, it contains the pointer to array, length and capacity (maximum length to which slice can extend).
## String, Rune, Character, Byte

Source: https://go.dev/blog/strings
- String in golang is slice of bytes
- String literals are always utf-8 encoded. (Go source code) eg `const nihongo = "日本語"`
- In unicode standard, each character is represented by "code point" eg, U+2318 represents `⌘` , in golang this code point is referred as rune (aliased to int32)
- When you range through a loop, it decodes 1 utf-8 length rune on each loop

## Time

- [Layout string in time](https://pkg.go.dev/time@go1.23.2#Time.Format).Parse and time.Format expects this date (reference date): 01/02/2006  `Jan 2 15:04:05 2006 MST` (Note the date should be this specific date and time for it to parse successfully). Following shows some example:

```
time.Parse("01/02/2006", "10/02/2024")
time.Parse("02 of 01 2006", "02 of 10 2024")
```

## Embed files in binary
- Use `embed` package to add files to binary at compile time

## Use local dependency

To use local version of the dependency, you can clone the deps in dir $DEP, then use replace directive in go mod

`$ go mod edit -replace github.com/google/go-cmp=$DEP`

## Import local modules

Import other packages rather than main package

```
import (
  "noc-manager/pkg/models"
)
```

Run `go mod edit -replace noc-manager=../../noc-manager` to add a local dependency & run `go mod tidy`

Tip: Name modules as simple names rather than git urls unless you're planning on publishing them. Otherwise you might get weird issues.
## CommandLine

- After parsing flags you can get other arguments via: `flag.Args()` (array) or `flag.Arg(i)` specific arg. `flag.Narg` = number of args

## Run debugger

```
$ go install github.com/go-delve/delve/cmd/dlv@latest

// in root dir
$ dlv debug
```
## Sql

- For database sql, checkout [this wiki](https://go.dev/wiki/SQLInterface)

## Slog

```
slog.Info(msg, k1, v1, k2, v2)
```

Log consists of log level, message, and key value pairs (it is assumed that key will follow value in above example). 
#### Levels

Some common levels include Info, Warn, Debug, Error. But since, log levels are integers, you can define your own custom levels.  
#### Handlers

```
logger := slog.NewTextHandler()
logger.Info(msg, user, os.Getenv(USER))
```

slog supports multiple handlers, you can even write your own custom handler. Some common handlers include:
- slog.NewTextHandler (prints key=value in text)
- slog.NewJSONHandler (prints key value in json)

Out of Box, if you don't use specific handler, it uses default Logger instance. 

- For more info, checkout docs: [slog](https://pkg.go.dev/log/slog)

## ToString equivalent

```
type Transaction struct {
  Amount          float64 `json:"amount"`
  Description     string  `json:"description"`
  TransactionDate string  `json:"transaction_date"`
}

func (t Transaction) String() string {
  return fmt.Sprintf("Amount: %f, Description: %s, Date: %s", t.Amount, t.Description, t.TransactionDate)
}
```

## Regexp 

```
package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`Rs\.(\d+(?:\.\d+)?) has been debited`)
	fmt.Printf("%q\n", re.FindStringSubmatch("Dear Customer, Rs.396.00 has been debited from account"))
}

["Rs.396.00 has been debited" "396.00"]
```

## Get error in string

```
s := err.Error()
```

## JSON or YAML omitempty or ignore

```
type T struct {
    F int `yaml:"a,omitempty"`
    B int `yaml:"-"` // this field will be ignored from rendering
}
```

```
type T struct {
    F int `json:"a,omitempty"`
    B int `json:"-"` // this field will be ignored from rendering
}
```

## Json Encoder/Decoder

`encodings/json` package has Encoder/Decoder, can be used as:

```
err := json.NewDecoder(resp.Body).Decode(&var)
```

it accepts any input which implements interfaces io.Reader or io.Writer (basically streaming data). Some core data sources which implement it are:
- os.File (read from file on disk)
- strings.Reader (allows to read string)
- http.Response.Body (http response)
- bytes.Buffer (similar to string, in memory buffer)
- net.Conn (allows reading from socket, tcp or udp)
## Desktop application in go

[Wails])(https://wails.io/) helps bootstrap a desktop app in go. Allows a choice of frontend like Vue.js etc. It automatically create front-end binding classes and functions from go structs.

## Data Indexing

[blevesearch/bleve](https://github.com/blevesearch/bleve) is a data indexing and search library in go. 
## Sources
- 
## Related
- [](Slack#Post%20to%20a%20channel%5D)
- [](Golang%20Language%5D)
- [](Golang%20Language%5D)
- [](Golang%20Language%5D)
