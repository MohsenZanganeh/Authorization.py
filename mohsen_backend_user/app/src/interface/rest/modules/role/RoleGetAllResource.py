from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.role.RoleGetAllUseCase import RoleGetAllUseCase
from src.domain.v1.role import RoleValidatore
role_schema = RoleValidatore().RoleGetSchema

class RoleGetAll(baseResource):
    def __init__(self):
        super().__init__()

    def get(self):
        # Validation
        
        role_json = self.query
        if role_json:
            role_schema(role_json)
        # UseCase
        return RoleGetAllUseCase().get_all(**self.query)