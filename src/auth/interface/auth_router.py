from fastapi import APIRouter, Depends , status
from .auth_schemas import RegisterRequest, LoginRequest, UserOut , DeleteResuest
from .dependencies import get_register_use_case, get_login_use_case , get_delete_use_case
from ..application.use_cases.register_user import RegisterUser
from ..application.use_cases.login_user import LoginUser
from ..application.use_cases.delete_user import DeleteUser


router = APIRouter(tags=["auth"], prefix="/auth")

@router.post("/register", response_model=UserOut)
async def register(
    request: RegisterRequest,
    use_case: RegisterUser = Depends(get_register_use_case)
):
    user = await use_case.execute(request.email, request.password)
    return UserOut.model_validate(user)

@router.post("/login", response_model=UserOut)
async def login(
    request: LoginRequest,
    use_case: LoginUser = Depends(get_login_use_case)
):
    user = await use_case.execute(request.email, request.password)
    return UserOut.model_validate(user)

@router.delete("/delete/{email}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    email:str,
    use_case : DeleteUser = Depends(get_delete_use_case)
):
    await use_case.execute(email)
