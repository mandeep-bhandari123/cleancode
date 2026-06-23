from abc import ABC , abstractmethod

class JWTService(ABC):
    @abstractmethod
    def create_token(self, user_id:str)->str:
        ...

    @abstractmethod
    def verify_token(self, token:str):
        """Returns user_id if valid, Raises InvalidTokenError of not"""
        ...
