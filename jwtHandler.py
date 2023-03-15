import time
import jwt
from decouple import config


class JWTHandler:

    @staticmethod
    def encode(user_id:str):
        payload ={
            "user_id":user_id,
            "expiry":time.time()+600
        }

        token = jwt.encode(payload,config("JWT_SECRET"), algorithm=config("JWT_ALGORITHM"))

        return token

    @staticmethod
    def decode(token:str):
        try:
            token = jwt.decode(token,config("JWT_SECRET"), algorithm=config("JWT_ALGORITHM"))
            if token and token['expiry'] >=time.time():
                return True
            else:
                return False
        except:
            return False

