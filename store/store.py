from abc import ABC

class Store(ABC):
    """A backend store that stores the mapping between shortened URL and original URL"""

    def add(self, short_url:str, url:str, user:str = None) -> bool:
        """
        Add the shortened URL and original URL pair into store.

        Parameters
        ----------
        short_url : str
            The shortened URL, it should not be None or Empty.
        url : str
            The original URL, it should not be None or Empty.
        user: str
            Optional, user's name who created this link

        Returns
        ----------
        bool: 
        If the shortened URL already exsits in the store, do nothing. Return True if the original URL is the same, otherwise return False.
        If the shortened URL does not exsit in the store, add the pair and return True.
        """
        raise NotImplementedError()

    def get(self, short_url:str) -> str:
        """
        Using the shortened URL key (without base_url) to retrieve the original URL.

        Parameters
        ----------
        short_url : str
            The shortened URL key, it should not be None or Empty and should not contain the base_url.

        Returns
        ----------
        str: 
        If the shortened URL key exists in the store, return the original URL. Otherwise return None.
        """
        raise NotImplementedError()

    def update(self, short_url:str, url:str, user:str) -> bool:
        """
        Update the shortened URL and original URL pair in the store.

        Parameters
        ----------
        short_url : str
            The shortened URL, it should not be None or Empty.
        url : str
            The original URL, it should not be None or Empty.
        user: str
            Required for update a URL, as the user only can update his/her own shortened URL. 

        Returns
        ----------
        bool: 
        If the shortened URL exsits in the store and the user is the creator, update the new URL to the store and return True.
        If the shortened URL does not exsit in the store, return False.
        """
        raise NotImplementedError()