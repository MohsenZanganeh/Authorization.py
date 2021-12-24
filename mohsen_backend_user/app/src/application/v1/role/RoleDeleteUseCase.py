
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db


class RoleDeleteUseCase():
    def __init__(self):
        self.role = db().role()

    def delete(self,props):
        
        role = self.role.delete(props['id'])
        if role:
            return SUCCESS('role was Deleted Successfully')
        else:
            raise BAD_REQUEST('role was Not Deleted')