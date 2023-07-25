#!/usr/bin/envvpython3

"""
    Module for a class called LIFOCache that
    inherits from the class BaseCaching
"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
        A class called LIFOCache that inherits from a
        base clas called BaseCaching and is a caching system
    """

    def __init__(self):
        """
            Overloads the __init_ method of the base class
        """

        super().__init__()

    def put(self, key, item):
        """
            adds new key/value pairs to be cached in the
            self.cache_data dictionary
        """

        if key and item:
            cached_data = self.cache_data
            cached_data.update({key: item})
            keys = [k for k in cached_data]

            if len(keys) > self.MAX_ITEMS:
                del cached_data[keys[-2]]
                print(f"DISCARD: {keys[-2]}")

    def get(self, key):
        """
            returns the value of key that is linked to
            self.cache_dat
        """

        if key and self.cache_data.get(key):
            return self.cache_data[key]
        return None
