#!/usr/bin/env python3
''' Basic cache Basic cache Basic cache Basic cache
'''

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' LRU cache class
    '''

    def put(self, key, item):
        '''puts item to key element'''
        if key and item:
            self.cache_data[key] = item
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                print("DISCARD:", first)
                self.cache_data.pop(first)

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
