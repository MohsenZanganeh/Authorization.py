
from datetime import timedelta
from flask_jwt_extended.utils import create_access_token, create_refresh_token
from src.interface.rest.constants.statusCodes import SUCCESS
from werkzeug.security import safe_str_cmp
from src.interface.rest.errors.ErrorHandler import INVALID_CREDENTIALS
from src.infrastructure.database.v1.nosql.mongo.db import db
# from src.infrastructure.contactServices.ContactProducer import contant_Produceres
class UserLoginUseCase():     
    def __init__(self):
        self.user = db().user() 
   
    def Login(self,props):

        user = self.user.get_one({'username':props['username']})
        if user and safe_str_cmp(props['password'], user['password']):
            user = self.user.updateByQuery({'username':props['username']},{'is_login': True})
            del user['password']
            del user['is_deleted']
            del user['activate']
            del user['update_at']
            del user['created_at']
            del user['is_active']

            user['id'] = user['_id']['$oid']
            del user['_id']
            
            access_token = create_access_token(
                identity=user,
                expires_delta=timedelta(minutes=50),
                 fresh=True
                 )
            
            refresh_token = create_refresh_token({'id':user['id']})
            
            return SUCCESS({'access_token': access_token, 'refresh_token': refresh_token})
        
        raise INVALID_CREDENTIALS('INVALID_CREDENTIALS')