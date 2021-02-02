from operations.base_operation_mongo.base_delete import BaseDelete


class MongoDelete(BaseDelete):

    def delete_one(self, record={}):
        """
        delete record in mongodb
        param record: json
        return: Bool
        """
        my_query = {'product_id': record["product_id"]}
        try:
            self.client.mclient[self.dbname][self.collectionName].delete_one(my_query)
            return True
        except Exception as e:
            return False

    def delete_many(self, record={}):
        try:
            self.client.mclient[self.dbname][self.collectionName].delete_many(record)
            return True
        except Exception as e:
            return False