
from bson.objectid import ObjectId
from src.interface.rest.modules.baseResource import baseResource
from flask_jwt_extended import jwt_required,get_jwt_identity
from src.application.v1.role.RoleDeleteUseCase import RoleDeleteUseCase
from src.domain.v1.role import RoleValidatore
role_schema = RoleValidatore().RoleDeleteSchema

class RoleDelete(baseResource):
    def __init__(self):
        super().__init__()

    def delete(self,id):

        role_json = self.query
        if role_json:
            role_schema(role_json)
        # UseCase
        return RoleDeleteUseCase().delete(self.query['_id'])