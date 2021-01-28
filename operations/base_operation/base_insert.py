from abc import ABC, abstractmethod


class BaseInsert(ABC, object):

    def __init__(self, _client=None, db_name=None, collection_name=None):
        self.client = _client
        self.dbname = db_name
        self.collectionName = collection_name

    @abstractmethod
    def insert_one(self, record={}):
        pass

    @abstractmethod
    def insert_many(self, records={}):
        pass
