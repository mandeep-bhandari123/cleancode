from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select , delete , update
from ...domain.entities import User , UserInDB, UserOut
from ...domain.repository import UserRepository
from ...infrastructure.orm.models import UserModel
from uuid import UUID


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self , session:AsyncSession):
        self.session = session

    async def create_user(self, user:User) ->UserInDB:
        db_user = UserModel(
            email = user.email,
            password_hash = user.password_hash
        )
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        return UserInDB(
            id = db_user.id,
            email=db_user.email,
            password_hash=db_user.password_hash
        )

    async def get_user_by_email(self  ,email:str )->UserInDB | None:
        result = await self.session.execute(select(UserModel).where(UserModel.email ==email))

        db_user = result.scalar_one_or_none()
        if not db_user:
            return None
        return UserInDB(
            id=db_user.id,
            email=db_user.email,
            password_hash=db_user.password_hash,
        )

    async def delete_user(self, email:str )->dict | None:
        await self.session.execute(
            delete(UserModel).where(UserModel.email == email)
        )

        await self.session.commit()

        return {"Message":"User already deleted"}

    async def update_user(self, user: User) -> UserInDB | None:
        result = await self.session.execute(
            select(UserModel).where(UserModel.email == user.email)
        )
        db_user = result.scalar_one_or_none()
        if not db_user:
            return None

        db_user.email = user.email
        db_user.password_hash = user.password_hash

        await self.session.commit()
        await self.session.refresh(db_user)

        return UserInDB(
            id=db_user.id,
            email=db_user.email,
            password_hash=db_user.password_hash,
        )
