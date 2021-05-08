from abc import ABC

class Store(ABC):
    """A backend store that stores the mapping between shortened URL and original URL"""

    def add(self, short_url:str, url:str) -> bool:
        """
        Add the shortened URL and original URL pair into store.

        Parameters
        ----------
        short_url : str
            The shortened URL, it should not be None or Empty.
        url : str
            The original URL, it should not be None or Empty.

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