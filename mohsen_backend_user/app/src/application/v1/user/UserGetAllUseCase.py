
from src.interface.rest.constants.statusCodes import SUCCESS
from src.interface.rest.errors.ErrorHandler import NOT_FOUND
from src.infrastructure.database.v1.nosql.mongo.db import db
# from src.infrastructure.contactServices.ContactProducer import contant_Produceres
class UserGetAllUseCase():     
    def __init__(self):
        self.user = db().user() 
   
    def get_all(self,**query):
        # role = self.role.get_all(is_deleted = False,**query)
        query['is_deleted'] = False
        user = self.user.get_all(query,join=True)

        if user:
            return SUCCESS(user)
        else:
            raise NOT_FOUND('role was Not Found')