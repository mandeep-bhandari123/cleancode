from fastapi import APIRouter, Depends
from .auth_schemas import RegisterRequest, LoginRequest, UserOut
from .dependencies import get_register_use_case, get_login_use_case
from ..application.use_cases.register_user import RegisterUser
from ..application.use_cases.login_user import LoginUser

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
