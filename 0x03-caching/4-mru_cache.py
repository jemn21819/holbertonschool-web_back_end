#!/usr/bin/python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Create a class MRUCache that
    inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """
        constructor
        """
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is not None and item is not None:
            self.timesKey[key] = self.time
            self.time += 1
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = None
            newer = self.time - 2

            for _key, _value in self.timesKey.items():
                if newer == _value:
                    discard_key = _key
                    break
            del self.cache_data[discard_key]
            del self.timesKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """
        get the cache item value
        """
        if key is None or key not in self.cache_data:
            return None
        self.timesKey[key] = self.time
        self.time += 1

        return self.cache_data[key]
