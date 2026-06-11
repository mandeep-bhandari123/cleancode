from dataclasses import dataclass
from uuid import UUID
@dataclass
class User:
    email:str
    password:str

@dataclass
class UserInDB(User):
    id:UUID

@dataclass
class UserOut():
    email:str
    id:UUID
