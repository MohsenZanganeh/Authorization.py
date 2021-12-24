from src.interface.rest.modules.baseResource import baseResource
from src.application.v1.user.UserRegisterUseCase import UserRegisterUseCase
from src.domain.v1.user import UserValidatore
user_schema = UserValidatore().UserCreateSchema


class UserRegister(baseResource):
    def __init__(self):
        super().__init__()

    def post(self):
        # Validation        
        user_json = self.props
        if user_json:
            user_json = user_schema(user_json)
        
        # UseCase
        return UserRegisterUseCase().Register(user_json)