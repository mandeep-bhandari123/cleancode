from contextlib import asynccontextmanager
from fastapi import FastAPI
from .auth.interface.auth_router import router as auth_router
from .auth.infrastructure.database import init_db
from .auth.interface.exception_handlers import (
    user_already_exists_handler,
    invalid_credentials_handler,
    user_not_found_handler
)
from .auth.domain.exceptions import (
    UserAlreadyExistsError,
    InvalidCredentialsError,
    UserNotFoundError
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

app.add_exception_handler(UserAlreadyExistsError, user_already_exists_handler)
app.add_exception_handler(InvalidCredentialsError, invalid_credentials_handler)
app.add_exception_handler(UserNotFoundError, user_not_found_handler)

@app.get("/")
async def root():
    return {"Mandeep Bhandari": "Benevolent dictator for life"}
