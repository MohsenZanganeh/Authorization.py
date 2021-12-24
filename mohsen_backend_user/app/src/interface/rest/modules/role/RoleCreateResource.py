from flask import request
from flask_restful import Resource
from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.role.RoleCreateUseCase import RoleCreateUseCase  
from src.domain.v1.role import RoleValidatore
role_schema = RoleValidatore().RoleCreateSchema

class RoleCreate(baseResource):
    def __init__(self):
        super().__init__()
        
    def post(self):
        # Validation
        role_json = self.props
        if role_json:
           role_json = role_schema(role_json)
        
        # UseCase
        return RoleCreateUseCase().create(role_json)