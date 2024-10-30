#!/usr/bin/env python3
"""MRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A caching system using Most Recently Used cache replacement algorithm
    """
    def __init__(self):
        """LRUCache class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache using MRU cache replacement algorithm
        """
        if key and item:
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                mru = list(self.cache_data.keys())[-2]
                del self.cache_data[mru]
                print("DISCARD: {}".format(mru))

    def get(self, key):
        """Get an item from the cache by key
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
