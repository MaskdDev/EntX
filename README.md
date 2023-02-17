# EntX - The Python Encryption Library

## EntX Encryption and Decryption

### How to create an encryption client with password stored in an environment variable:
```
import os
import entx

client = entx.Client(os.environ["password"])
```

### How to encrypt a string
```
import os
import entx

client = entx.Client(os.environ["password"])
to_encrypt = "This will be encrypted"
encrypted = client.encrypt(to_encrypt)
```

### How to decrypt a string
```
import os
import entx

client = entx.Client(os.environ["password"])
to_decrypt = "This will be decrypted"
encrypted = client.decrypt(to_decrypt)
```

## EntX Storage

### JSON
EntX supports JSON reading and writing, allowing you to store and read dictionaries in the .json format, automatically encrypting and decrypting the data with the password provided.

#### How to create a JSON client with a password stored in an environment variable:
```
import os
from entx.storage import JSONClient

client = JSONClient(os.environ["password"])
```

#### How to convert a dictionary to an encrypted JSON string:
```
import os
from entx.storage import JSONClient

client = JSONClient(os.environ["password"])
to_encrypt_dictionary = {"keys": "values"}
dictionary_json_string = client.dumps(to_encrypt_dictionary)
```

#### How to write a dictionary to an encrypted JSON file:
```
import os
from entx.storage import JSONClient

client = JSONClient(os.environ["password"])
to_encrypt_dictionary = {"keys": "values"}
with open("demo.json", "w") as output_file:
    client.dump(to_encrypt_dictionary, output_file)
```

#### How to read a dictionary from an encrypted JSON string:
```
import os
from entx.storage import JSONClient

client = JSONClient(os.environ["password"])
encrypted_json_string = "your string here"
decrypted_dictionary = client.loads(encrypted_json_string)
```

#### How to read a dictionary from an encrypted JSON file:
```
import os
from entx.storage import JSONClient

client = JSONClient(os.environ["password"])
with open("demo.json", "r") as input_file:
    decrypted_dictionary = client.load(input_file)
```