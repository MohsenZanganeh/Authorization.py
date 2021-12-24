from bson.objectid import ObjectId
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST, NOT_FOUND
from src.interface.rest.constants.statusCodes import SUCCESS

from src.infrastructure.database.v1.nosql.mongo.db import db


class RoleUpdateUseCase():
    def __init__(self):
        database = db()
        self.role = database.role()
        self.permission = database.permission()

    def update(self, id, props):
        get_role = self.role.get_one({'_id': id})
        if get_role is None:
            raise NOT_FOUND('role was not found')

        if props.get('permissions'):

            def permissions_func(x): return x['permission_id']
            permissions_mapped = list(
                map(permissions_func, props.get('permissions')))

            length_permissions_mapped = len(set(permissions_mapped))

            if len(props.get('permissions')) != length_permissions_mapped:
                raise BAD_REQUEST('you entered a permission twice')

            permissions = self.permission.get_all(
                {'_id': {'$in': permissions_mapped}})

            if len(permissions) < length_permissions_mapped:
                raise BAD_REQUEST('one of the permissions id not found')
                                 
        role = self.role.updateByQuery({"_id": id}, props)
        if role:
            return SUCCESS('role was Updated Successfully', id=role)
        else:
            raise BAD_REQUEST('role was Not Updated')
