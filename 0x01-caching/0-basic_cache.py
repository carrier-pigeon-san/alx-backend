#!/usr/bin/env python3
"""BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """Constructor"""
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the cache
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
