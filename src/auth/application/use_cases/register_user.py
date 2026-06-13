from src.auth.domain.exceptions import UserALreadyExistsError
from ..ports.password_hasher import AbstractPasswordHasher
from src.auth.domain.repository import UserRepository
from src.auth.domain.entities import User

class RegisterUser:
    def __init__(self, repo:UserRepository, hasher:AbstractPasswordHasher):
        self.repo = repo
        self.hasher = hasher

    async def execute (self, email:str , password:str):
        if (await self.repo.get_user_by_email(self.email)):
            raise UserALreadyExistsError()
        else:
            hashed_password = self.hasher.hash(plain_password=password)
            user = User(email=email , password_hash=hashed_password)
            saved_user = await self.repo.create_user(user)
            return saved_user

