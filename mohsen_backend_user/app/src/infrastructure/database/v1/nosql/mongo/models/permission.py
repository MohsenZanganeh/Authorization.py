from src.infrastructure.database.v1.nosql.mongo.models.AbstractRepository import AbstractRepository
from pymongo import ASCENDING
from pymongo.operations import IndexModel
def Create_Permission_Schema(db):
    model = db.create_collection('permission', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['title'],
            'properties': {
                'title': {
                    'bsonType': 'string',
                    'description': 'set a title to permission'
                },
                'path': {
                    'bsonType': 'string'
                },
                'method': {
                    'bsonType': 'string'
                },
                'group': {
                    'bsonType': 'string',
                    'description': 'all role can have this permission or not'
                },
                'is_generic': {
                    'bsonType': 'bool',
                    'description': 'all role can have this permission or not'
                },
                'is_public': {
                    'bsonType': 'bool',
                    'description': 'this permission is public for all user or not'
                },
                'is_admin': {
                    'bsonType': 'bool',
                    'description': 'this permission is just for admins'
                }
            }
        }
    })

    title = IndexModel([('title', ASCENDING)], unique=True)
    model.create_indexes([title])

class PermissionModel(AbstractRepository):
    def __init__(self, db):
        # relations = [
        #     {'field': 'template_id', 'model': 'template'},
        # ]
        self.model = db.get_collection('permission')
        super().__init__(db,self.model)