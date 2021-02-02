try:
    from abc import ABC, abstractmethod
except Exception as e:
    print("Error: {} ".format(e))


class BaseUpdate(ABC, object):

    def __init__(self, _client=None, index=None, doc_type=None):
        self.client = _client
        self.index = index
        self.doc_type = doc_type

    @abstractmethod
    def update_one(self, query, id=id):
        pass

    def update_unique(self, query, id=id):
        pass
