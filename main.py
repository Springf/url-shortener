from shortener import hash_shortener
from store.in_memory_store import InMemoryStore
from validator import regex_validator

class Shortener():
    def __init__(self, shortener, store, validator) -> None:
        self.shortener = shortener
        self.store =  store
        self.validator = validator
    
    def shorten(self, url) -> str:
        shortened_str = ''
        
        if self.validator(url):
            shortened_str = self.shortener(url)
            # 3 is an arbitrary number here to prevent collision
            i = 0
            while i < 3 and not self.store.add(shortened_str, url):
                shortened_str = self.shortener(url)
        else:
            raise ValueError("URL is invalid.")    

        if not shortened_str:
            raise ValueError('Failed to shorten the URL.')
        return shortened_str

    def retrieve(self, shortened_str) -> str:
        url = ''
        url = self.store.get(shortened_str)
            
        if not url:
            raise ValueError('Failed to find the URL.')
        
        return url


if __name__ == '__main__':
    shortener = Shortener(hash_shortener.shorten, InMemoryStore(), regex_validator.validate)
    command = input("Please enter the command (shorten: s url, retrieve: r shorturl):")
    while command:
        if command[0] == 's':
            print(shortener.shorten(command[2:]))
        if command[0] == 'r':
            print(shortener.retrieve(command[2:]))
        command = input("Please enter the command (shorten: s url, retrieve: r shorturl):")
