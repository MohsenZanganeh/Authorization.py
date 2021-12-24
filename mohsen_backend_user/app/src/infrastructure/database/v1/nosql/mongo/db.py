from src.infrastructure.database.v1.nosql.mongo.models import user,permission,role
import config
from pymongo import MongoClient


class db():

    def __init__(self):
        self.client = MongoClient(
            config.MONGO['host'],
            config.MONGO['port'],
            username=config.MONGO['username'],
            password=config.MONGO['password'])[config.MONGO['database']]

    def user(self):
        if ('user' in self.client.list_collection_names()) == False:
            user.Create_User_Schema(self.client)
        return user.UserModel(self.client)
    
    def role(self):
        if ('role' in self.client.list_collection_names()) == False:
            role.Create_Role_Schema(self.client)
        return role.RoleModel(self.client)
    
    def permission(self):
        if ('permission' in self.client.list_collection_names()) == False:
            permission.Create_Permission_Schema(self.client)
        return permission.PermissionModel(self.client)