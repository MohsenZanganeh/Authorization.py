from datetime import datetime
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError, WriteError
from src.infrastructure.database.v1.nosql.mongo.models.AbstractRepository import AbstractRepository


def Create_User_Schema(db):
    db.create_collection('user', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['username', 'password'],
            'properties': {
                'username': {
                    'bsonType': 'string',
                    'description': 'set a username for user'
                },
                'password': {
                    'bsonType': 'string',
                    'description': 'set a password for user'
                },
                "roles": {
                    'bsonType': 'array',
                    'items': {
                        'bsonType': 'objectId'
                    }
                },
                'is_admin': {
                    'bsonType': 'bool'
                },
                'is_super_admin': {
                    'bsonType': 'bool'
                },
                'is_login': {
                    'bsonType': 'bool',
                    'description': 'recognizing user is login or not'
                }
            }
        }
    })


class UserModel(AbstractRepository):
    def __init__(self, db):
        # relations = [
        #     {'field': 'template_id', 'model': 'template'},
        # ]
        self.model = db.get_collection('user')
        super().__init__(db, self.model)

    def update(self, id, data):
        try:
            set_query = {}
            if data.get('roles'):
                set_query['$addToSet'] = {'roles': {'$each': data['roles']}}
                del data['roles']

            set_query['$set'] = data
            set_query['$set']['update_at'] = datetime.now()

            self.model.update_one({'_id': ObjectId(id)}, set_query)
            return str(id)
        except DuplicateKeyError as err:
            self._duplicate_error_handler(err)
        except WriteError as err:
            self._write_error_handler(err)
