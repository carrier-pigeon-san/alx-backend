#!/usr/bin/env python3
""" LFUCache module """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ A caching system based on Least Frequently Used cache replacement
    algorithm.
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.frequency = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache with LFU algorithm. """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 0
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            for i, (k, v) in enumerate(self.frequency.items()):
                if i == 0:
                    lfu = k
                    lfu_v = v
                    continue
                if i == len(self.frequency) - 1:
                    break
                if v < lfu_v:
                    lfu = k
                    lfu_v = v
            del self.cache_data[lfu]
            del self.frequency[lfu]
            print("DISCARD: {}".format(lfu))

    def get(self, key):
        """ Get an item by key using LFU cache replacement algorithm """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        return self.cache_data[key]
