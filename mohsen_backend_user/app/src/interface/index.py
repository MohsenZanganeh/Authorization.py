from src.interface.rest.modules.user import \
    UserLoginResource,\
    UserLogoutResource,\
    UserRegisterResource,\
    UserGetAllResource,\
    UserGetOneResource,\
    UserUpdateResource

from src.interface.rest.modules.role import \
    RoleUpdateResource,\
    RoleCreateResource,\
    RoleDeleteResource,\
    RoleGetAllResource,\
    RoleGetOneResource

from src.interface.rest.modules.permission import \
    PermissionGetAllResource,\
    PermissionGetOneResource,\
    PermissionCreateManyResource

resources_dict = {
    'user': [
        [UserLoginResource.UserLogin,       '/login'],
        [UserLogoutResource.UserLogout,     '/logout'],
        [UserRegisterResource.UserRegister, '/register'],
        [UserUpdateResource.UserUpdate,     '/<string:id>'],
        [UserGetOneResource.UserGetOne,     '/<string:id>'],
        [UserGetAllResource.UserGetAll,     '/']
    ],
    'role': [
        [RoleCreateResource.RoleCreate, '/'],
        [RoleUpdateResource.RoleUpdate, '/<string:id>'],
        [RoleDeleteResource.RoleDelete, '/<string:id>'],
        [RoleGetOneResource.RoleGetOne, '/<string:id>'],
        [RoleGetAllResource.RoleGetAll, '/']
    ],
    'permission': [
        [PermissionCreateManyResource.PermissionCreateAll, '/create-many'],
        [PermissionGetOneResource.PermissionGetOne, '/<string:id>'],
        [PermissionGetAllResource.PermissionGetAll, '/']
    ]
}
