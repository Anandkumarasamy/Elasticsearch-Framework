__NAME__ = "Indranil Samanta"
__VERSION__ = "0.1"

try:
    import os
    import io
    import sys
    import json
    from pymongo import MongoClient
    from bson.objectid import ObjectId
except Exception as e:
    print("Error: {} ".format(e))


class Singleton(type):
    """This is a Singleton Design Pattern"""
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """Creates only one instance of the class"""
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Settings(metaclass=Singleton):

    def __init__(self, host=None, maxpoolsize=50, port=27010):
        self.host = host
        self.maxPoolSize = maxpoolsize
        self.port = port


class Client(metaclass=Singleton):

    def __init__(self, _settings=None):
        self.settings = _settings
        self.mclient = MongoClient(host=self.settings.host,
                                   port=self.settings.port,
                                   maxPoolSize=self.settings.maxPoolSize)
