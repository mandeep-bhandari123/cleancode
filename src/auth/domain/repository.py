from abc import ABC, abstractmethod
from src.auth.domain.entities import User , UserInDB, UserOut
from uuid import UUID


class UserRepository(ABC):

    @abstractmethod
    async def create_user(self, user:User)->UserInDB:
        """Creates User"""
        ...


    @abstractmethod
    async def get_user_by_email(self, email:str)->UserOut |None:
        """Gets User by email"""
        ...

    @abstractmethod
    async def update_user(self , user_id:UUID, user_update:dict)->UserOut | None:
        """Updates User"""
        ...


    @abstractmethod
    async def delete_user(self, user_id: UUID )->None:
        """Delete User"""
        ...
