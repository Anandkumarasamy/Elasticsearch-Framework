class ElasticDelete(object):

    def __init__(self, _client=None, index=None, doc_type=None):
        self.client = _client
        self.index = index
        self.doc_type = doc_type

    def delete_one(self, id=id):
        """
        update record in Elasticsearch
        param record: json
        return: Bool
        """

        try:
            respon = self.client.elastic.update(index=self.index,
                                                doc_type=self.doc_type,
                                                id=id)
            return True
        except Exception as e:
            return False