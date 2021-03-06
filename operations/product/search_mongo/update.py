from operations.base_operation_mongo.base_update import BaseUpdate


class MongoUpdate(BaseUpdate):

    def update_one(self, record={}):
        """
        update record in mongodb
        param record: json
        return: Bool
        """
        my_query = {'product_id': record["product_id"]}
        new_value = {"$set": record}
        try:
            if self.client.mclient[self.dbname][self.collectionName].find(my_query).count() > 0:
                self.client.mclient[self.dbname][self.collectionName].update_one(my_query, new_value)
                return True
        except Exception as e:
            return False

    def update_quantity(self, record={}):
        my_query = {'product_id': record["product_id"],
                    'product_sellers.seller_id': record["seller_id"],
                    'product_sellers.product_info.product_version': record["product_version"]}
        new_value = {"$inc": {"product_sellers.0.product_info.number_of_products": -record["number_of_products"]}}
        try:
            if self.client.mclient[self.dbname][self.collectionName].find(my_query).count() > 0:
                self.client.mclient[self.dbname][self.collectionName].update(my_query, new_value)
                return True
        except Exception as e:
            return False
