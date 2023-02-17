# EntX - The Python Encryption Library

## How to create an encryption client with password stored as an environment variable:
```
import os
import entx
client = entx.Client(os.environ["password"])
```

## How to encrypt a string
```
import os
import entx
client = entx.Client(os.environ["password"])
to_encrypt = "This will be encrypted"
encrypted = client.encrypt(to_encrypt)
```

## How to decrypt a string
```
import os
import entx
client = entx.Client(os.environ["password"])
to_decrypt = "This will be decrypted"
encrypted = client.decrypt(to_decrypt)
```