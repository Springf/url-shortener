from shortener import hash_shortener
import hashlib
import base64

def test_url_happy():
    test_url = 'https://www.google.com'
    assert base64.b64encode(hashlib.sha256(f'{test_url}0'.encode('utf-8')).digest()).decode()[0:8] == hash_shortener.shorten(test_url)

def test_url_retry():
    test_url = 'https://www.yahoo.com'
    assert base64.b64encode(hashlib.sha256(f'{test_url}2'.encode('utf-8')).digest()).decode()[0:8] == hash_shortener.shorten(test_url, 2)