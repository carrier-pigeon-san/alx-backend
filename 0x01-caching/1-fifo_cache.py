#!/usr/bin/env python3
"""FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that implements First In First Out cache replacement
    policy
    """
    def __init__(self):
        """Class constructor"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache using FIFO cache replacement algorithm
        """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                old = list(self.cache_data.keys())[0]
                del self.cache_data[old]
                print("DISCARD: {}".format(old))

    def get(self, key):
        """Get an item from the cache by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
