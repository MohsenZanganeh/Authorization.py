
from src.interface.rest.constants.statusCodes import SUCCESS
from werkzeug.security import safe_str_cmp
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.infrastructure.database.v1.nosql.mongo.db import db
# from src.infrastructure.contactServices.ContactProducer import contant_Produceres
class UserUpdateUseCase():     
    def __init__(self):
        self.user = db().user() 
 
    def update(self,id,props):
        
        user = self.user.updateById(id,props)
        if user:
            return SUCCESS('user was Updated Successfully',id = user)
        else:
            raise BAD_REQUEST('user was Not Updated')