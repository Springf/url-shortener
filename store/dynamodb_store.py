from .store import Store

class DynamoDBStroe(Store):
    def __init__(self) -> None:
        super().__init__()
    
    def add(self, short_url:str, url:str) -> bool:
        return ''
