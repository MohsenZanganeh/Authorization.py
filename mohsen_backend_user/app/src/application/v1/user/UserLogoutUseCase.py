
from bson.objectid import ObjectId
from src.interface.rest.constants.statusCodes import SUCCESS
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.infrastructure.database.v1.nosql.mongo.db import db
from flask import request
class UserLogoutUseCase():    
    def __init__(self):
        self.user = db().user() 

    def Logout(self,user_payload):
        user = self.user.updateById(ObjectId(user_payload['_id']['$oid']),{'login':False})
        if user:
            return SUCCESS('user was logout Successfully')
        else:
            raise BAD_REQUEST('user was Not logout')