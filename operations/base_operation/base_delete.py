from abc import ABC, abstractmethod


class BaseDelete(ABC, object):

    def __init__(self, _client=None, db_name=None, collection_name=None):
        self.client = _client
        self.dbname = db_name
        self.collectionName = collection_name

    @abstractmethod
    def delete_one(self, record={}):
        pass

    @abstractmethod
    def delete_many(self, records={}):
        pass