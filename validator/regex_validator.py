import re

"""
Implements a "very" basic regular expression based validator for the URL.
In real world more sophisticated approach could be taken like checking against a scam database to prevent scam URLs.
"""

def validate(url:str) -> bool:
    pattern = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\._]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
    return re.search(pattern, url) is not None
