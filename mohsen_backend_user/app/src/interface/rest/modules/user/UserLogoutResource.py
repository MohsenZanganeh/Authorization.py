
from src.application.v1.user.UserLogoutUseCase import UserLogoutUseCase
from src.interface.rest.modules.baseResource import baseResource
from src.domain.v1.user import UserValidatore

user_schema = UserValidatore().UserCreateSchema

class UserLogout(baseResource):
    def __init__(self):
        super().__init__()

    def put(cls):
        
        # UseCase
        return UserLogoutUseCase().Logout()