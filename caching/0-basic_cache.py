#!/usr/bin/env python3
'''
class BasicCache that inherits from BaseCaching and is a caching system
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Basic Cache class '''

    def put(self, key, item):
        '''puts item to key'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''get key from cache_data'''
        if key in self.cache_data:
            return self.cache_data[key]
