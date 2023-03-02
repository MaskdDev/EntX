import hashlib
import random

encryption_style = """aYb1AcX8dWe4fB!IUg-L0{hi:,;/\CjTk2Hl&V_m7@nDMo^pJ)5q E#Nr>+st9$FR*"Q=ZuP<Kv(%O3w}GxS6yz"""

def generatePasswordSeed(password: str):
    # Initialise variables
    count = 1
    seed = 0
    factor = 1
    
    # Get password hash
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Get multiplication factor from hash
    for char in pass_hash:
        if char.lower() in ["a", "r", "t"]:
            factor += 1
            
    # Generate seed
    for char in pass_hash * factor:
        try:
            charcode = ord(char)
        except:
            charcode = 0  
        seed += (count * charcode)
        count += 1
    
    # Return seed
    return seed

def generatePasswordEncryption(password: str):
    # Get and set password seed
    seed = generatePasswordSeed(password)
    random.seed(seed)
    
    # Shuffle with random seed
    encryption_style_split = [char for char in encryption_style]
    random.shuffle(encryption_style_split)
    custom_encryption_style = "".join(encryption_style_split)
    
    # Return custom styling
    return custom_encryption_style

def encryptkit(to_encrypt: str, password: str):
    # Initialise Variables
    encrypted = ""
    
    # Get password encryption
    encryption = generatePasswordEncryption(password)
    
    # Encrypt using new encryption style
    index = 0
    for char in str(to_encrypt):
        if char in encryption:
            char_position = encryption.find(char)
            new_char_position = (char_position + len(password) * ord(encryption[len(password)]) + index) % 87
            encrypted += encryption[new_char_position]
        else:
            encrypted += char
        index = index + 1
            
    # Return final result
    return encrypted

def decryptkit(to_decrypt: str, password: str):
    # Initialise Variables
    decrypted = ""
    
    # Get password encryption
    encryption = generatePasswordEncryption(password)
    
    # Decrypt using new encryption style
    index = 0
    for char in str(to_decrypt):
        if char in encryption:
            char_position = encryption.find(char)
            old_char_position = (char_position - len(password) * ord(encryption[len(password)]) - index) % 87
            decrypted += encryption[old_char_position]
        else:
            decrypted += char
        index = index + 1
            
    # Return final result
    return decrypted

def apply_map(obj: dict, func):
    if isinstance(obj, dict):
        new_obj = {}
        for key in obj:
            if isinstance(obj[key], dict):
                new_obj[func(key)] = apply_map(obj[key], func)
            elif isinstance(obj[key], str) or isinstance(obj[key], int) or isinstance(obj[key], float):
                new_obj[func(key)] = func(obj[key])
            elif isinstance(obj[key], list):
                new_obj[func(key)] = [func(item) for item in obj[key]]
                
        # Return finished dictionary
        return new_obj
    
    else:
        raise TypeError("obj must be an instance of dict.")