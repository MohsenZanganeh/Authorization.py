
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db


class PermissionDeleteUseCase():
    def __init__(self):
        self.permission = db().permission()

    def delete(self,props):
        
        permission = self.permission.delete(props['id'])
        if permission:
            return SUCCESS('permission was Deleted Successfully')
        else:
            raise BAD_REQUEST('permission was Not Deleted')