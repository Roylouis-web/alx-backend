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
                time = None
                found_key = None
                count = 0

                for k, v in timestamp.items():
                    if count == 0:
                        time = v["time"]
                    if v["time"] > time:
                        time = v["time"]
                        found_key = k
                    count += 1

                del cached_data[found_key]
                del timestamp[found_key]
                print(f"DISCARD: {found_key}")

            timestamp.update({key: {"time": datetime.now()}})

    def get(self, key):
        """
            returns a value that links to self.cache_data
        """

        if key and self.cache_data.get(key):
            self.timestamp[key]["time"] = datetime.now()
            return self.cache_data[key]
        return None
