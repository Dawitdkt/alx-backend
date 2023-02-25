#!/usr/bin/python3
""" LFU Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.lfu = {}  # store the frequency of each key
        self.lru = {}  # store the recency of each key

    def put(self, key, item):
        """Assign the item to the key in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item  # update the value
            self.lfu[key] += 1  # increase the frequency
            self.lru[key] = len(self.lru)  # update the recency
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # find the least frequency used key
                min_freq = min(self.lfu.values())
                lfu_keys = [k for k, v in self.lfu.items() if v == min_freq]
                if len(lfu_keys) == 1:
                    # only one key with minimum frequency
                    lfu_key = lfu_keys[0]
                else:
                    # more than one key with minimum frequency
                    # use LRU algorithm to break ties
                    min_rec = min(self.lru[k] for k in lfu_keys)
                    lfu_key = [
                        k for k in lfu_keys if self.lru[k] == min_rec][0]
                print("DISCARD: {}".format(lfu_key))
                del self.cache_data[lfu_key]  # discard the key
                del self.lfu[lfu_key]  # remove from frequency dict
                del self.lru[lfu_key]  # remove from recency dict

            self.cache_data[key] = item  # add the new key and value
            self.lfu[key] = 1  # set the initial frequency to 1
            self.lru[key] = len(self.lru)  # set the initial recency to max

    def get(self, key):
        """Return the value associated with the key in the cache"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self.lfu[key] += 1  # increase the frequency of access
        self.lru[key] = len(self.lru)  # update the recency of access
        return value
