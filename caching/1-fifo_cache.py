#!/usr/bin/env python3
'''
class FIFOCache that inherits from BaseCaching and is a caching system
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Fifo cache class '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''puts item to key element'''
        if key and item:
            self.cache_data[key] = item
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD:", first)
                self.cache_data.pop(first)

    def get(self, key):
        '''get key from cache_data'''
        if key in self.cache_data:
            return self.cache_data[key]
