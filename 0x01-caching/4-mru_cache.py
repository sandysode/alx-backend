#!/usr/bin/python3
"""MRU Cache Class"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    An implementation of MRU Cache

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
            keyOut = self.__cacheUpdate(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """ Get an item by key

        Args:
            key: key of the dict item
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__keys:
                self.__cacheUpdate(key)
        return value

    def __cacheUpdate(self, keyIn):
        """ Removes the earliest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(keysLength - 1)
                    self.cache_data.pop(keyOut)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(keysLength, keyIn)
        return keyOut
