from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.user.UserUpdateUseCase import UserUpdateUseCase  
from src.domain.v1.user import UserValidatore
user_schema = UserValidatore().UserUpdateSchema

class UserUpdate(baseResource):
    def __init__(self):
        super().__init__()

    def put(self,id):
        # Validation
        user_json = self.query
        if user_json:
            user_schema(user_json)
        
        # UseCase
        return UserUpdateUseCase().update(self.query['_id'],user_json)