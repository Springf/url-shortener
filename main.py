from core.shortener import hash_shortener
from store.in_memory_store import InMemoryStore
from core.validator import regex_validator
from core import api

"""
A command line utility to show case how to interact with the shortener core api.
An in memory store is implemented to store the URLs.
Usage:
s url -> returns the shortened URL token
r token -> return the original URL
"""
if __name__ == '__main__':
    shortener = api.Shortener(hash_shortener.shorten, InMemoryStore(), regex_validator.validate)
    command = input("Please enter the command (shorten: s url, retrieve: r token):")
    while command:
        try:
            if command[0] == 's':
                print(shortener.create(command[2:]))
            if command[0] == 'r':
                print(shortener.retrieve(command[2:]))
        except ValueError as e:
            print(e)
        command = input("Please enter the command (shorten: s url, retrieve: r token):")
       
