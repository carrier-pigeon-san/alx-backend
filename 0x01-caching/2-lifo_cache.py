#!/usr/bin/env python3
"""LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A caching system that implements Last In First Out cache replacement
    policy
    """
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache using LIFO cache replacement algorithm
        """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                new = list(self.cache_data.keys())[-2]
                del self.cache_data[new]
                print("DISCARD: {}".format(new))

    def get(self, key):
        """Get an item from the cache by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
