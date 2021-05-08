from .store import Store
from threading import RLock

class InMemoryStore(Store):
    def __init__(self) -> None:
        super().__init__()
        self.__store = dict()
        self.__lock = RLock()
    
    def add(self, short_url:str, url:str) -> bool:
        if not short_url or not url:
            return False

        with self.__lock:
            if short_url in self.__store:
                if url == self.__store[short_url]:
                    return True
                else:
                    return False
            else:
                self.__store[short_url] = url
        return True

    def get(self, short_url:str) -> str:
        if not short_url:
            return None
        print(self.__store)
        print(short_url)
        if short_url in self.__store:
            return self.__store[short_url]
        return None
