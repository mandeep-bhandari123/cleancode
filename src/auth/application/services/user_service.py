from src.auth.domain.repository import  UserRepository
from src.auth.domain.entities import User

class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def validate_user(self, user: User):
        await self.__check_uniqueness(user)

    async def __check_uniqueness(self, user: User):
        existing_user = await self.user_repo.get_user_by_email(
            user.email
        )

        if existing_user:
            raise Exception("User with same email already exists")

  