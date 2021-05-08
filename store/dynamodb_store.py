from .store import Store
import boto3
from botocore.exceptions import ClientError

class DynamoDBStroe(Store):
    def __init__(self) -> None:
        super().__init__()
        self.__store = boto3.client('dynamodb')
        self.__url_key = 'url'
        self.__user_key = 'user'
        self.__table = 'url_store'
        self.__partition_key = 'shortened_url'
    
    def add(self, short_url:str, url:str, user:str = None) -> bool:
        if not short_url or not url:
            raise ValueError('URL cannot be empty.')
        item={
            self.__partition_key:short_url,
            self.__url_key:url,
            self.__user_key:user
        }
        try:
            self.__store.put_item(TableName = self.__table, Item=item, ConditionExpression=f'attribute_not_exists({self.__partition_key})')
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
                return False
            else:
                raise

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
        try:
            if short_url in self.__store:
                if user != self.__store[short_url][self.__user_key]:
                    return False
                else:
                    self.__store[short_url] = {self.__url_key:url, self.__user_key:user}
                    return True
            else:
                return False
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
                return False
            else:
                raise
