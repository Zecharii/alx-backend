#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.access_time = {}
        self.time = 0

    def put(self, key, item):
        """ Add an item in the cache using LFU
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.access_time[key] = self.time
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used item(s)
                    min_freq = min(self.frequency.values())
                    lfu_keys =
                    [k for k, v in self.frequency.items() if v == min_freq]

                    if len(lfu_keys) > 1:
                        # If there are ties, use LRU to determine removal
                        lfu_key =
                        min(lfu_keys, key=lambda k: self.access_time[k])
                    else:
                        lfu_key = lfu_keys[0]

                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    del self.access_time[lfu_key]

                # Add new item
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.access_time[key] = self.time

            self.time += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.access_time[key] = self.time
        self.time += 1
        return self.cache_data[key]
