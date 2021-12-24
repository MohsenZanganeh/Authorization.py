
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db

class UserRegisterUseCase():
    def __init__(self):
        self.user = db().user() 

    def Register(self,props):

        if self.user.get_one({'username': props['username'], 'is_deleted': False}):
            raise BAD_REQUEST('Duplicate')
        
        user = self.user.insert(props)
        if user:
            return SUCCESS('User was Created Successfully')
        else:
            return BAD_REQUEST('User was Not Created')