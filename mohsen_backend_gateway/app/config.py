import os

DEBUG = True

MONGO = {
    'host': 'mohsen-mongo',
    'port': 27017,
    'database': 'mohsen_user',
    'username': 'mohsen',
    'password': '123'
}

REDIS = {
    'host':'mohsen-redis',
    'port': 6379,
    'db': 0
}
SERVER = os.getenv('SERVER_URL')
SERVICES = {
    'user':'5002',
    'permission':'5002',
    'role':'5002',
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access','refresh']
