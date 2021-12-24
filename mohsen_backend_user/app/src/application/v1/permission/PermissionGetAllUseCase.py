
from src.interface.rest.errors.ErrorHandler import NOT_FOUND
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db


class PermissionGetAllUseCase():
    def __init__(self):
        self.permission = db().permission()      

    def get_all(self,**query):
        # permission = self.permission.get_all(is_deleted = False,**query)
        query['is_deleted'] = False
        permission = self.permission.get_all(**query,join=True)

        if permission:
            return SUCCESS(permission)
        else:
            raise NOT_FOUND('permission was Not Found')