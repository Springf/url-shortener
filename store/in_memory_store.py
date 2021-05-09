from core.store.store import Store
from threading import RLock

class InMemoryStore(Store):
    def __init__(self) -> None:
        super().__init__()
        self.__store = dict()
        self.__lock = RLock()
        self.__url_key = 'url'
        self.__user_key = 'user'
    
    def add(self, short_url:str, url:str, user:str = None) -> bool:
        if not short_url or not url:
            raise ValueError('URL cannot be empty.')
        with self.__lock:
            if short_url in self.__store:
                if url == self.__store[short_url][self.__url_key]:
                    return True
                else:
                    return False
            else:
                if user:
                    self.__store[short_url] = {self.__url_key:url, self.__user_key:user}
                else:
                    self.__store[short_url] = {self.__url_key:url}
        return True

    def get(self, short_url:str) -> str:
        if not short_url:
            raise ValueError('URL cannot be empty.')
        print(self.__store)
        print(short_url)
        if short_url in self.__store:
            return self.__store[short_url][self.__url_key]
        return None
    
    def update(self, short_url:str, url:str, user:str) -> bool:
        if not short_url or not url or not user:
            raise ValueError('URL or user cannot be empty.')
        with self.__lock:
            if short_url in self.__store:
                if user != self.__store[short_url][self.__user_key]:
                    return False
                else:
                    self.__store[short_url] = {self.__url_key:url, self.__user_key:user}
                    return True
            else:
                return False
