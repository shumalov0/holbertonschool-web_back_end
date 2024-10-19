#!/usr/bin/env python3
''' Basic cache Basic cache Basic cache Basic cache
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFO cache class
    '''

    def put(self, key, item):
        ''' Add an item in the cache
            and remove first if more than max items
        '''
        if key and item:
            if self.cache_data.__len__() + 1 > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem()
                print("DISCARD:", last[0])
            self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key
        '''
        if key in self.cache_data:
            return self.cache_data[key]
