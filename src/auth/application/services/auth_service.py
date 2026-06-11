from src.auth.application.interfaces.password_hasher import AbstractPasswordHasher

class AuthService:
    def __init__(self, hasher:AbstractPasswordHasher):
        self.hasher = hasher

    async def hash_password(self , plain_password:str)->str:
        return self.hasher.hash(plain_password)

    async def verify_password(self , plain_password:str , hashed_password:str)->bool:
        return self.hasher.verify(plain_password, hashed_password)

