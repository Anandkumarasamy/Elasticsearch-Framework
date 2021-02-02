from operations.base_operation_elasticsearch.base_update import BaseUpdate


class ElasticUpdate(BaseUpdate):

    def update_one(self, query, id=id):
        """
        update record in Elasticsearch
        param record: json
        return: Bool
        """

        try:
            response = self.client.elastic.update(index=self.index,
                                                  doc_type=self.doc_type,
                                                  id=id,
                                                  body=query)
            return True
        except Exception as e:
            return False