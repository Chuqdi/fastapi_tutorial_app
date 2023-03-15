


from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from jwtHandler import JWTHandler




class JwtBearer(HTTPBearer):
    def __init__(self, auto_error:bool=True ):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credetials:HTTPAuthorizationCredentials = await super().__call__(request)
        print(credetials)

        
        if (len(credetials.scheme) < 1) or  (not credetials.scheme == "Bearer"):
            print("Is")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Error")
        else:
            return credetials.credentials
        
        
    
    def verify_jwt(self, token:str):
        return JWTHandler.decode(token)


