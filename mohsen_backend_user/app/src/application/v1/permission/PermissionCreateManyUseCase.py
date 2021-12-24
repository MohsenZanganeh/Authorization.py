
from src.interface.rest.errors.ErrorHandler import BAD_REQUEST
from src.interface.rest.constants.statusCodes import SUCCESS
from src.infrastructure.database.v1.nosql.mongo.db import db
from src.infrastructure.seeder.PermissionSeeder import create_permissions

class PermissionCreateManyUseCase():
    def __init__(self):
        self.permission = db().permission()

    def create(self,props):
        create_permissions(props)