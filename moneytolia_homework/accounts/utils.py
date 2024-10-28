import random
import string
import time
import hashlib

def generate_api_key():
    # Generate a random part of the key
    random_part = "".join(random.choices(string.ascii_letters + string.digits, k=25))
    
    # Add a timestamp-based part for uniqueness
    timestamp = str(int(time.time()))
    
    # Concatenate and hash for extra security
    raw_key = timestamp + random_part
    hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()[:30]
    
    return f"{timestamp}-{hashed_key}"
