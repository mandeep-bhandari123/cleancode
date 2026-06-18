from src.auth.domain.exceptions import UserNotFoundError
from ..ports.password_hasher import AbstractPasswordHasher
from src.auth.domain.repository import UserRepository
from src.auth.domain.entities import User

class DeleteUser():
    def __init__(self, repo:UserRepository):
        self.repo = repo

    async def execute(self, email:str ):
        user =await self.repo.get_user_by_email(email)
        if(not user ):
            raise UserNotFoundError()
        await self.repo.delete_user(email)


