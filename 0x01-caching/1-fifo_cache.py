#!/usr/bon/env python3

"""
    Module for a subclass called FIFOCache
    that inherits from BaseCaching class
"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
        A class calles FIFOCache that inherits from a
        base class called BaseCaching and is a caching system
    """

    def __init__(self):
        """
            Overloads the __init__ method of the base class
        """

        super().__init__()

    def put(self, key, item):
        """
            Assigns a new key/value pair to self.cache_data
        """

        if key and item:
            cached_data = self.cache_data
            cached_data.update({key: item})
            keys = [k for k in cached_data]

            if len(keys) > self.MAX_ITEMS:
                del cached_data[keys[0]]
                print(f"DISCARD: {keys[0]}")

    def get(self, key):
        """
            returns the value in self.cache_data
            linked to key
        """

        if key and self.cache_data.get(key):
            return self.cache_data[key]
        return None
