
from src.interface.rest.errors.ErrorHandler import NOT_FOUND
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db


class RoleGetAllUseCase():
    def __init__(self):
        self.role = db().role()      

    def get_all(self,**query):
        # role = self.role.get_all(is_deleted = False,**query)
        query['is_deleted'] = False
        role = self.role.get_all(query,join=True)

        if role:
            return SUCCESS(role)
        else:
            raise NOT_FOUND('role was Not Found')