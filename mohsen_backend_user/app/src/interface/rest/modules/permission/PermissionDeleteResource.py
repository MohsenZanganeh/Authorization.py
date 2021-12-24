
from bson.objectid import ObjectId
from src.interface.rest.modules.baseResource import baseResource
from flask_jwt_extended import jwt_required,get_jwt_identity
from src.application.v1.permission.PermissionDeleteUseCase import PermissionDeleteUseCase
from src.domain.v1.permission import PermissionValidatore
permission_schema = PermissionValidatore().PermissionDeleteSchema


class PermissionDelete(baseResource):
    def __init__(self):
        super().__init__()

    def delete(self):
        
        permission_json = self.query
        if permission_json:
            permission_schema(permission_json)
        # UseCase
        return PermissionDeleteUseCase().delete(self.query['_id'])