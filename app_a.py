from pydantic import BaseSettings # Only exists in v1

class Cfg(BaseSettings):
    message: str = "Hello from app a!"

print(Cfg().dict())