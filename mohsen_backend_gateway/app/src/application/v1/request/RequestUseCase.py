
import json
from json.decoder import JSONDecodeError
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST, FORBIDDEN, NOT_FOUND
from src.interface.rest.constants.statusCodes import SUCCESS
from src.infrastructure.database.v1.nosql.redis.db import rdb 
from src.infrastructure.database.v1.nosql.mongo.db import db 
import requests
import config
from flask import request
from utils.jwt import verify_token
class RequestUseCase():
    def __init__(self):
        self.permission = db().permission()

    def request(self,headers,url_rule,original_url,method,body={},query={}):
        
        permission = self.permission.get_one({'path': url_rule,'method':method.lower()})
        generated_url = self._generate_url(original_url,permission['group'])
        if permission:
            if permission.get('is_public') == True:
                response = requests.request(method=method,url = f'http://{generated_url}',json=body)
                data = json.loads(response.text)
                return data
            else:
        
                if "Authorization" in headers:
                    user = verify_token(headers['Authorization'])
                    user = user['sub']
                    has_access = rdb().hget(
                        f"{permission['path']}-{method.lower()}",
                        user['id'])

                    if has_access:
                        body['user'] = user
                        response = requests.request(method=method,url = f'http://{generated_url}',json=body)
                        try:
                            data = json.loads(response.text)
                            return SUCCESS(data)
                        except JSONDecodeError as err:
                            raise BAD_REQUEST(response.text)
                            
                raise FORBIDDEN('FORBIDDEN')
        else:
            raise NOT_FOUND('NOT_FOUND')

            
    def _generate_url(self,url,service):
        return f'{config.SERVER}:{config.SERVICES.get(service)}{url}'
    