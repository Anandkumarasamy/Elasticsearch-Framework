try:
    from abc import ABC, abstractmethod
except Exception as e:
    print("Error: {} ".format(e))


class BaseDelete(ABC, object):
    def __init__(self, _client=None, index=None, doc_type=None):
        self.client = _client
        self.index = index
        self.doc_type = doc_type

    @abstractmethod
    def delete_one(self, id=id):
        pass

    @abstractmethod
    def delete_many(self, record=[]):
        pass