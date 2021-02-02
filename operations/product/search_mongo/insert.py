from operations.base_operation_mongo.base_insert import BaseInsert


class MongoInsert(BaseInsert):

    def insert_one(self, record={}):
        """
        insert record in mongodb
        param record: json
        return: Bool
        """
        try:
            self.client.mclient[self.dbname][self.collectionName].insert_one(record)
            return True
        except Exception as e:
            return False

    def insert_many(self, record=[]):
        try:
            self.client.mclient[self.dbname][self.collectionName].insert_many(record)
            return True
        except Exception as e:
            return False