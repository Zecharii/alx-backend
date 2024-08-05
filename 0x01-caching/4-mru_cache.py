#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """ Add an item in the cache using MRU
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data:
                # Remove the most recently used item (MRU)
                if self.mru_key is not None:
                    print(f"DISCARD: {self.mru_key}")
                    del self.cache_data[self.mru_key]

            # Add new item or update existing item
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the most recently used key
        self.mru_key = key
        return self.cache_data[key]
