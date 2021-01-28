from operations.base_operation.base_delete import BaseDelete


class MongoDelete(BaseDelete):

    def delete_one(self, record={}):
        """
        delete record in mongodb
        param record: json
        return: Bool
        """
        my_query = {'product_id': record["product_id"]}
        try:
            if self.client.mclient[self.dbname][self.collectionName].find(my_query).count() > 0:
                self.client.mclient[self.dbname][self.collectionName].delete_one(my_query)
                return True
        except Exception as e:
            return False

    def delete_many(self, record={}):
        return False