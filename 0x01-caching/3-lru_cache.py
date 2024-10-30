#!/usr/bin/env python3
"""LRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A caching system using Least Recently Used cache replacement algorithm
    """
    def __init__(self):
        """LRUCache class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache using LRU cache replacement algorithm
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
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
