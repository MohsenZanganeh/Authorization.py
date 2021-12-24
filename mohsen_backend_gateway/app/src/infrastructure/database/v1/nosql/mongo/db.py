from src.infrastructure.database.v1.nosql.mongo.models import permission
import config
from pymongo import MongoClient


class db():

    def __init__(self):
        self.client = MongoClient(
            config.MONGO['host'],
            config.MONGO['port'],
            username=config.MONGO['username'],
            password=config.MONGO['password'])[config.MONGO['database']]
    
    def permission(self):
        if ('permission' in self.client.list_collection_names()) == False:
            permission.Create_Permission_Schema(self.client)
        return permission.PermissionModel(self.client)
    