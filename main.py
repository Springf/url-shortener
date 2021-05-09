from core.shortener import hash_shortener
from store.in_memory_store import InMemoryStore
from core.validator import regex_validator
from core import api

if __name__ == '__main__':
    shortener = api.Shortener(hash_shortener.shorten, InMemoryStore(), regex_validator.validate)
    command = input("Please enter the command (shorten: s url, retrieve: r shorturl):")
    while command:
        if command[0] == 's':
            print(shortener.create(command[2:]))
        if command[0] == 'r':
            print(shortener.retrieve(command[2:]))
        command = input("Please enter the command (shorten: s url, retrieve: r shorturl):")
