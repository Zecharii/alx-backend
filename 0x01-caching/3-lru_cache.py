#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the existing item
                self.usage_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item (LRU)
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add new item or update existing item
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key and update the usage order
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data.get(key)
