from ..infrastructure.repositories.sqlalchemy_user_repo import SQLAlchemyUserRepository
from ..infrastructure.security.bcrypt_hasher import BcryptPasswordHasher
from ..application.use_cases.register_user import RegisterUser
from..application.use_cases.login_user import LoginUser
from ..application.use_cases.delete_user import DeleteUser
from sqlalchemy.ext.asyncio import AsyncSession
from ..infrastructure.database import get_db
from fastapi import Depends

async def get_register_use_case(session :AsyncSession = Depends(get_db)):
    repo = SQLAlchemyUserRepository(session=session)
    hasher = BcryptPasswordHasher()
    return RegisterUser(repo=repo , hasher=hasher)

async def get_login_use_case(session :AsyncSession = Depends(get_db)):
    repo = SQLAlchemyUserRepository(session=session)
    hasher = BcryptPasswordHasher()
    return LoginUser(repo=repo , hasher=hasher)

async def get_delete_use_case(session :AsyncSession = Depends(get_db)):
    repo = SQLAlchemyUserRepository(session=session)
    return DeleteUser(repo = repo )
