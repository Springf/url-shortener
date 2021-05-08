import hashlib
import base64

"""
Implements a basic shortener algorithem use the SHA256 hash function and truncate to 8 characters in base64.
Because base64 packs more bits in a single character than Hex representation, we got slightly more collission resistance here.
Remove the special chars from the base64 encoding for URL safety.
"""

def shorten(url:str, retry = 0) -> str:
    return base64.b64encode(hashlib.sha256(f'{url}{retry}'.encode('utf-8')).digest()).decode().replace('+','').replace('/','').replace('=','')[0:8]
