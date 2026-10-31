from pydantic import BaseModel # Only exists in v2

class Cfg(BaseModel):
    message: str = "Hello from app b!"

print(Cfg().model_dump())