from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.user.UserGetAllUseCase import UserGetAllUseCase  
from src.domain.v1.user import UserValidatore
user_schema = UserValidatore().UserGetSchema
class UserGetAll(baseResource):
    def __init__(self):
        super().__init__()

    def get(self):
        # Validation
        
        
        user_json = self.query
        if user_json:
            user_schema(user_json)
        # UseCase
        return UserGetAllUseCase().get_all(**self.query)