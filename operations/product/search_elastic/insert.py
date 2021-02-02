try:
    from elasticsearch import helpers
except Exception as e:
    print("Error: {} ".format(e))

from operations.base_operation_elasticsearch.base_insert import BaseInsert


class ElasticInsert(BaseInsert):

    def insert_one(self, record={}):
        """
        insert record in Elasticsearch
        param record: json
        return: Bool
        """
        try:
            response = self.client.elastic.index(index=self.index,
                                                 doc_type=self.doc_type,
                                                 body=record)
            return True
        except Exception as e:
            return False

    def insert_many(self, record={}):
        """
        insert many record in Elasticsearch
        param record: json
        return: Bool
        """
        try:
            response = helpers.bulk(self.client.elastic, record,
                                    index=self.index,
                                    doc_type=self.doc_type)

            return True
        except Exception as e:
            return False
