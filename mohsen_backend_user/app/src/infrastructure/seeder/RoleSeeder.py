from bson.objectid import ObjectId
from src.infrastructure.database.v1.nosql.mongo.db import db
from src.infrastructure.database.v1.nosql.redis.db import rdb
from swagger.swagger import swagger


def create_role():
    database = db()
    role_model = database.role()
    permission_model = database.permission()
    user_model = database.user()

    user = user_model.get_one({'is_super_admin': True})
    if user is None:
        user = user_model.insert({
            "username": "superadmin",
            "password": "123",
            "is_admin": False,
            "is_super_admin": True,
            "is_login": False,
            "activate": True
        })
    else:
        user = user['_id']['$oid']

    permissions = permission_model.get_all({'is_deleted': False})
    generated_permissions = []
    for permission in permissions:
        generated_permissions.append({
            '_id': ObjectId(permission['_id']['$oid']),
            'title': permission['title']
        })

        path_generated = f"{permission['path']}-{permission['method']}"

        if len(rdb().hkeys(path_generated)) == 0:
            rdb().hset(path_generated, user, 1)

    role = role_model.get_one({'title': 'Super Admin'})
    if role is None:
        role = role_model.insert({
            'title': 'Super Admin',
            'permissions': generated_permissions,
            'is_assignable': False,
            'is_visible': False,
            'is_readonly': True
        })
    else:
        for permission in generated_permissions:
            is_exist_permission = role_model.get_one(
                {'permissions': {'$elemMatch': {'title': permission['title']}}})
            if is_exist_permission is None:
                role_model.update(role['_id']['$oid'],{'permissions':permission})
        role = role['_id']['$oid']
    

    user_model.update(user, {'roles': [ObjectId(role)]})
