import jwt
from datetime import datetime , timedelta , timezone
from application.ports.jwt_service import JWTService
from domain.exceptions import InvalidTokenError

class PyJWTService(JWTService):
    def __init__(self, secret_key: str, algorithm: str = "HS256", expire_minutes: int = 30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes

    def create_token(self, user_id: str) -> str:
        payload = {
            "sub": user_id,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=self.expire_minutes),
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> str:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload["sub"]
        except jwt.PyJWTError:
            raise InvalidTokenError("Invalid or expired token")
