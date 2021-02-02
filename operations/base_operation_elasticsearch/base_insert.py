try:
    from abc import ABC, abstractmethod
except Exception as e:
    print("Error: {} ".format(e))


class BaseInsert(ABC, object):

    def __init__(self, _client=None, index=None, doc_type=None):
        self.client = _client
        self.index = index
        self.doc_type = doc_type

    @abstractmethod
    def insert_one(self, record={}):
        pass

    @abstractmethod
    def insert_many(self, records={}):
        pass