__NAME__ = "Anand and Indranil Elastic framwork"
__VERSION__ = "0.1"

try:
    import uuid
    from elasticsearch import Elasticsearch
except Exception as e:
    print("Error: {} ".format(e))


class Metaclass(type):
    """This is a Singleton Design Pattern"""
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """Creates only one instance of the class"""
        if cls not in cls._instance:
            cls._instance[cls] = super(Metaclass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Settings(metaclass=Metaclass):
    def __init__(self, host=None, timeout=30, port=9200):
        self.host = host
        self.timeout = timeout
        self.port = port


class ElasticClient(metaclass=Metaclass):

    def __init__(self, _settings=None):
        self.settings = _settings
        host = self.settings.host
        self.elastic = Elasticsearch([{"host": self.settings.host,
                                       "port": self.settings.port}],
                                     timeout=self.settings.timeout)
