from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.user.UserLoginUseCase import UserLoginUseCase  
from src.domain.v1.user import UserValidatore
user_schema = UserValidatore().UserLoginSchema
class UserLogin(baseResource):
    def __init__(self):
        super().__init__()

    def post(self):
        # Validation        
        user_json = self.props
        if user_json:
            user_json = user_schema(user_json)
        
        # UseCase
        return UserLoginUseCase().Login(user_json)