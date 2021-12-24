from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.permission.PermissionUpdateUseCase import PermissionUpdateUseCase
from src.domain.v1.permission import PermissionValidatore
permission_schema = PermissionValidatore().PermissionUpdateSchema


class PermissionUpdate(baseResource):
    def __init__(self):
        super().__init__()

    def put(self):
        # Validation
        permission_json = {**self.props,**self.query}
        if permission_json:
           permission_json = permission_schema(permission_json)
        # UseCase
        return PermissionUpdateUseCase().update(self.query['_id'],permission_json)