#!/usr/bin/env python3

"""
    A class called LFUCache that inherits from a base
    class BaseCaching
"""

from datetime import datetime


BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
        A class called LRUCaching that inherits from
        BaseCaching class and implements caching using
        Least Recently Used algorithm
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
            timestamp.update({key: {"count": 1}})

            if len(cached_data) > self.MAX_ITEMS:
                count = 0
                found_key = None

                for v in timestamp.values():
                    if v["count"] > count:
                        count = v["count"]

                for k, v in timestamp.items():
                    if v["count"] < count:
                        count = v["count"]
                        found_key = k

                del cached_data[found_key]
                del timestamp[found_key]
                print(f"DISCARD: {found_key}")

    def get(self, key):
        """
            returns a value that links to self.cache_data
        """

        if key and self.cache_data.get(key):
            self.timestamp[key]["count"] += 1
            return self.cache_data[key]
        return None
