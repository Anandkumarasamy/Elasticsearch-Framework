from operations.base_operation_elasticsearch.base_delete import BaseDelete


class ElasticDelete(BaseDelete):

    def delete_one(self, id=id):
        """
        delete record in Elasticsearch
        param record: json
        return: Bool
        """

        try:
            response = self.client.elastic.delete(index=self.index,
                                                  doc_type=self.doc_type,
                                                  id=id)
            return True
        except Exception as e:
            return False

    def delete_many(self, record=[]):
        """
        delete many record in Elasticsearch
        param record: json
        return: Bool
        """
        query = []
        for doc_id in record:
            sub_query = {"delete": {"_index": self.index, "_type": self.doc_type, "_id": doc_id["_id"]}}
            query.append(sub_query)

        try:
            response = self.client.elastic.bulk(query)
            return True
        except Exception as e:
            return False