from ..ports.password_hasher import AbstractPasswordHasher
from src.auth.domain.repository import UserRepository
from ...domain.exceptions import InvalidCredentialsError
class LoginUser:
    def __init__(self, repo:UserRepository, hasher:AbstractPasswordHasher):
        self.repo = repo
        self.hasher = hasher

    async def execute(self , email:str , password:str):
        user = self.repo.get_user_by_email(email)
        if not user:
            raise InvalidCredentialsError()
        if not self.hasher.verify(password):
            raise InvalidCredentialsError()
        return user

