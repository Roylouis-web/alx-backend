#!/usr/bin/env python3

"""
    Module for a caching subclass named BasicCache
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
        A class called BasicCache that
        inherits from BaseCaching class
    """

    def put(self, key, item):
        """
            Assigns to the public instance attribute
            'self.cache_data' a new key/value pair
            to be cached
        """

        if key and item:
            cached_data = self.cache_data
            cached_data.update({key: item})

    def get(self, key):
        """
            returns the value in self.cache_data
            linked to the key
        """

        cached_data = self.cache_data
        if key and cached_data.get(key):
            return cached_data.get(key)
        return None
