from ..ports.password_hasher import AbstractPasswordHasher
from src.auth.domain.repository import UserRepository
from ...domain.exceptions import InvalidCredentialsError, UserNotFoundError

class UpdateUser:
    def __init__(self, repo: UserRepository, hasher: AbstractPasswordHasher):
        self.repo = repo
        self.hasher = hasher

    async def execute(self, email: str, password: str | None = None):
        user = await self.repo.get_user_by_email(email)
        if not user:
            raise UserNotFoundError()

        if password:
            user.password_hash = self.hasher.hash(password)

        await self.repo.update_user(user)
        return user
