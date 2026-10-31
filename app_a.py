from pydantic import BaseSettings

class Cfg(BaseSettings):
    gruss: str = "Hallo von App A"

print(Cfg().dict())