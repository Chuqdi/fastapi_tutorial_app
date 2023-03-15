from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hasher:
    @staticmethod
    def bcrypt(password):
        return pwd_cxt.hash(password)
    
    @staticmethod
    def deCrypt(password, encodedPassword):
        return pwd_cxt.verify(password, encodedPassword)
