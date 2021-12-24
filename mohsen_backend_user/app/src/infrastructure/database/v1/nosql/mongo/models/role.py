from datetime import datetime
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError, WriteError
from src.infrastructure.database.v1.nosql.mongo.models.AbstractRepository import AbstractRepository


def Create_Role_Schema(db):
    db.create_collection('role', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['title'],
            'properties': {
                'title': {
                    'bsonType': 'string',
                    'description': 'set a username for user'
                },
                'permissions': {
                    'bsonType': 'array',
                    'items': {
                        'bsonType': 'object',
                        'properties': {
                            'not_allowed': {
                                'bsonType': 'array',
                                'items': {
                                    'type': 'string'
                                }
                            },
                            '_id': {
                                'bsonType': 'objectId'
                            }
                        }
                    }
                },
                'is_assignable': {
                    'bsonType': 'bool',
                    'description': 'this role can assign to a normal'
                },
                'is_visible': {
                    'bsonType': 'bool',
                    'description': 'this permission is public for all user or not'
                },
                'is_readonly': {
                    'bsonType': 'bool',
                    'description': 'normal user can edit or not'
                }
            }
        }
    })


class RoleModel(AbstractRepository):
    def __init__(self, db):
        # relations = [
        #     {'field': 'template_id', 'model': 'template'},
        # ]
        self.model = db.get_collection('role')
        super().__init__(db, self.model)
        
    def update(self, id, data):
        try:
            set_query = {}
            if data.get('permissions'):
                set_query['$addToSet'] = {'permissions':{'$each': [data['permissions']]}}
                del data['permissions']

            set_query['$set'] = data
            set_query['$set']['update_at'] = datetime.now()
            self.model.update_one({'_id': ObjectId(id)}, set_query)
            return str(id)
        except DuplicateKeyError as err:
            self._duplicate_error_handler(err)
        except WriteError as err:
            self._write_error_handler(err)