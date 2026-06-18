from pydantic import BaseModel , EmailStr
from uuid import UUID
class RegisterRequest(BaseModel):
    email:EmailStr
    password:str

class LoginRequest(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:UUID
    email:EmailStr

    model_config = {"from_attributes": True}

class DeleteResuest(BaseModel):
    email:EmailStr
    password:str
