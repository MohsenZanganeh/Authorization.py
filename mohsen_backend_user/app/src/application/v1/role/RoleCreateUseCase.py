
from bson.objectid import ObjectId
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST, NOT_FOUND
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db

class RoleCreateUseCase():
    def __init__(self):
        database = db()
        self.role = database.role()
        self.permission = database.permission()

    def create(self,props):
        
        def permissions_func(x): return x['permission_id']
        permissions_mapped = list(
            map(permissions_func, props.get('permissions')))

        length_permissions_mapped = len(set(permissions_mapped))

        if len(props.get('permissions')) != length_permissions_mapped:
            raise BAD_REQUEST('you entered a permission twice')
            
        for permission in props['permissions']:
            get_permission = self.permission.get_one({'_id':ObjectId(permission['permission_id'])})
            if get_permission is None:
                raise NOT_FOUND('one of the permissions was not found')
            permission['title'] = get_permission['title']

        if self.role.get_one({'title': props['title']}):
            raise BAD_REQUEST('Duplicate')

        role = self.role.insert(props)
        if role:
            return SUCCESS('role was Created Successfully',id = role)
        else:
            raise BAD_REQUEST('role was Not Created')