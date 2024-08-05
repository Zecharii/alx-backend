#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache using LIFO
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data:
                # Remove the most recently added item (LIFO)
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    self.cache_data.pop(self.last_key)

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
