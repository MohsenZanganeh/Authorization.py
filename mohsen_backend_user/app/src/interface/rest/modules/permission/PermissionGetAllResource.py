from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.permission.PermissionGetAllUseCase import PermissionGetAllUseCase
from src.domain.v1.permission import PermissionValidatore
permission_schema = PermissionValidatore().PermissionGetSchema
class PermissionGetAll(baseResource):
    def __init__(self):
        super().__init__()

    def get(self):
        # Validation
        
        permission_json = self.query
        if permission_json:
           permission_json = permission_schema(permission_json)

        # UseCase
        return PermissionGetAllUseCase().get_all(**self.query)