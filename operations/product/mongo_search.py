from config.product_config.mongo_connection import Settings, Client
from operations.product.search_mongo.insert import MongoInsert
from operations.product.search_mongo.update import MongoUpdate


class Mongoose(object):
    """
    facade design pattern
    """

    def __init__(self, host=None, port=27010, maxpoolsize=50, dbname=None, collection_name=None):
        # creates an instance of settings class
        self._settings = Settings(host=host, port=port, maxpoolsize=maxpoolsize)
        # creates a single instance of client object
        self.client = Client(_settings=self._settings)
        self.dbname = dbname
        self.collectionName = collection_name

        self.insert = MongoInsert(_client=self.client, db_name=self.dbname, collection_name=self.collectionName)
        self.update = MongoUpdate(_client=self.client, db_name=self.dbname, collection_name=self.collectionName)
