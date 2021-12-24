from jwt import decode,ExpiredSignatureError,InvalidTokenError
import os
from src.interface.rest.errors.ErrorHandler import INVALID_CREDENTIALS
key = os.getenv('JWT_SECRET_KEY')
def verify_token(token):
    token = token.replace('Bearer ',"")
    try:
        return decode(token,key,algorithms=["HS256"])
    except ExpiredSignatureError:
        raise INVALID_CREDENTIALS('Your Token Has Expierd')
    except ExpiredSignatureError:
        raise INVALID_CREDENTIALS('Your Token Is Not Valid')