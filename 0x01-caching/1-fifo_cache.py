#!/usr/bin/python3
"""FIFO Cache Replacemet Implementatn Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    An implementation of FIFO Cache

    Attributes:
        __keys (list): Stores cache keys
        __rlock (RLock): Lock accessed resources
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key: key of the dict item
            item: value to be added
        """
        if key is not None and item is not None:
            key_out = self._cacheUpdate(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print('DISCARD: {}'.format(key_out))

    def get(self, key):
        """ Get an item by key

         Args:
            key: key of the dict item
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _cacheUpdate(self, key_in):
        """ Method to handle cache size and eviction"""
        key_out = None
        with self.__rlock:
            if key_in not in self.__keys:
                keysLength = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = self.__keys.pop(0)
                    self.cache_data.pop(key_out)
                self.__keys.insert(keysLength, key_in)
        return key_out
