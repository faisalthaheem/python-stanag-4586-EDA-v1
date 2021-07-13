# Python package for STANAG 4586 Edition A Version 1
## Tested with python 3.8x

Published branch | Development branch
--- | ---
![build status main branch](https://travis-ci.com/faisalthaheem/python-stanag-4586-EDA-v1.svg?branch=main) | ![build status development branch](https://travis-ci.com/faisalthaheem/python-stanag-4586-EDA-v1.svg?branch=development)

This repository conotains code that will enable encoding/decoding of STANAG messages.
So far the following messages have been implemented which should enable basic communication with a platform, messages are being continually added, please check back soon for updates.
- Message wrapper
- 01
- 20
- 21
- 200
- 300
- 301
- 302
- 1200
- 20000 [Private message for EO Pan and Tilt functionality]
- 20010 [Private message for query request]
- 20020 [Private message for query response]

> _*See further below for simple usage.*_

# Important note

 Please note this is a low level library and does not provide any network I/O or message assembly/disassembly.

Take a look at the [python-stanag-4586-vsm](https://github.com/faisalthaheem/python-stanag-4586-vsm) library which provides a basic implementation of a vehicle specific module (VSM) and uses this library to respond to discover, authorization and control messages.


# Simple usage example
Assuming you would have already parsed the message wrapper and know what message is contained in the byte array, save the following in a file called stanag-test.py

```python
from stanag4586edav1.message01 import *

# We create a dummy byte stream containing only Message 01 contents
PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\x00\x00\x00\xA0\x00\x00\x00\x00" \
b"\x00\x00\x00\x00\x00\x39\x00\x00\x01\x00\x00\x00\x00\x01\x00"


def decode_message01():
    msg01 = Message01(PACKET_TO_DECODE)
    
    print(msg01.time_stamp)
    print(msg01.cucs_id)

decode_message01()
```

Executing the above code will produce output as follows

```shell
$ python stanag-test.py
0.0
160

```