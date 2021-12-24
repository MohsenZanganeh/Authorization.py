
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db

class PermissionUpdateUseCase():
    def __init__(self):
        self.permission = db().permission()    

    def update(self,id,props):
        
        permission = self.permission.updateById(id,props)
        if permission:
            return SUCCESS('permission was Updated Successfully',id = permission)
        else:
            raise BAD_REQUEST('permission was Not Updated')