from pydantic import BaseModel

class Cfg(BaseModel):
    gruss: str = "Hallo von App B"

print(Cfg().model_dump())