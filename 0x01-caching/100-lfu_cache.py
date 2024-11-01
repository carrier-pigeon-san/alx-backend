#!/usr/bin/env python3
"""LFUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system using Least Frequently Used cache replacement algorithm
    """
    def __init__(self):
        """LFUCache class constructor"""
        super().__init__()
        self.frequency = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache using LFU cache replacement algorithm
        """
        if key and item:
            self.cache_data.update({key: item})
            self.frequency.update({key: 0})
            if len(self.cache_data) > self.MAX_ITEMS:
                for i, (k, v) in enumerate(self.frequency.items()):
                    if i == 0:
                        least = k
                        least_v = v
                        continue
                    if v < least_v:
                        least = k
                        least_v = v
                self.frequency.pop(least)
                self.cache_data.pop(least)
                print("DISCARD: {}".format(least))

    def get(self, key):
        """Get an item from the cache by key
        """
        if key and key in self.cache_data:
            self.frequency[key] += 1
            self.frequency.move_to_end(key)
            return self.cache_data.get(key)
        return None
