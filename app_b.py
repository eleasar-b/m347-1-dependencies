from pydantic import BaseModel # Only exists in v2

class Cfg(BaseModel):
    gruss: str = "Hallo von App B"

print(Cfg().model_dump())