from config.product_config.elastic_connection import Settings, ElasticClient
from operations.product.search_elastic.insert import ElasticInsert
from operations.product.search_elastic.update import ElasticUpdate
from operations.product.search_elastic.delete import ElasticDelete


class ElasticSearch(object):
    """
    facade design pattern
    """

    def __init__(self, host=None, port=9200, timeout=30, index=None, doc_type=None):
        # creates an instance of settings class
        self._settings = Settings(host=host, port=port, timeout=timeout)
        # creates a single instance of client object
        self.client = ElasticClient(_settings=self._settings)
        self.index = index
        self.doc_type = doc_type

        self.insert = ElasticInsert(_client=self.client, index=self.index, doc_type=self.doc_type)
        #self.update = ElasticUpdate(_client=self.client, index=self.index, doc_type=self.doc_type)
        #self.delete = ElasticDelete(_client=self.client, index=self.index, doc_type=self.doc_type)
        #self.get = ElasticGet(_client=self.client, index=self.index, doc_type=self.doc_type)