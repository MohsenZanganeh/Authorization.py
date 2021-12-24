from flask import request
from flask_restful import Resource
from src.application.v1.permission.PermissionCreateManyUseCase import PermissionCreateManyUseCase 

class PermissionCreateAll(Resource):
    @classmethod
    def post(cls):
        
        # UseCase
        return PermissionCreateManyUseCase().create(request.get_json())