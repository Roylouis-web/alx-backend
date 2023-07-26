#!/usr/bin/env python3

"""
    A class called LRUCache that inherits from a base
    class BaseCaching
"""

from datetime import datetime


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
        A class called MRUCaching that inherits from
        BaseCaching class and implements caching using
        Most Recently Used algorithm
    """

    def __init__(self):
        """
            Overloads the __init__ method of the base class
        """

        super().__init__()
        self.timestamp = {}

    def put(self, key, item):
        """
            add new key/value pairs to the public instance
            attribute self.cache_data of the super class
        """

        if key and item:
            cached_data = self.cache_data
            timestamp = self.timestamp
            cached_data.update({key: item})

            if len(cached_data) > self.MAX_ITEMS:
                time_list = [
                        v["time"] for v in timestamp.values()
                ]
                time = max(time_list)
                found_key = [
                        k for k, v in timestamp.items()
                        if v["time"] == time
                ]
                del cached_data[found_key[0]]
                del timestamp[found_key[0]]
                print(f"DISCARD: {found_key[0]}")

            timestamp.update({key: {"time": datetime.now()}})

    def get(self, key):
        """
            returns a value that links to self.cache_data
        """

        if key and self.cache_data.get(key):
            self.timestamp[key]["time"] = datetime.now()
            return self.cache_data[key]
        return None
