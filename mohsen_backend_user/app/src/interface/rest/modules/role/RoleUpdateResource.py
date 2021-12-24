from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.role.RoleUpdateUseCase import RoleUpdateUseCase
from src.domain.v1.role import RoleValidatore
role_schema = RoleValidatore().RoleUpdateSchema


class RoleUpdate(baseResource):
    def __init__(self):
        super().__init__()

    def put(self,id):
        # Validation
        role_json = {**self.props,**self.query}
        if role_json:
           role_json = role_schema(role_json)
        
        # UseCase
        return RoleUpdateUseCase().update(self.query['_id'],role_json)