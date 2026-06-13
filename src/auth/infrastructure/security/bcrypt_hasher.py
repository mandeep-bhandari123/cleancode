from passlib.context import CryptContext
from src.auth.application.ports.password_hasher import AbstractPasswordHasher

class BcryptPasswordHasher(AbstractPasswordHasher):

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, plain_password: str) -> str:
        return self.pwd_context.hash(plain_password)

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
