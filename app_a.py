from pydantic import BaseSettings # Only exists in v1

class Cfg(BaseSettings):
    gruss: str = "Hallo von App A"

print(Cfg().dict())