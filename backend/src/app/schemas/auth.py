from pydantic import BaseModel

class LoginRequest(BaseModel):
    identifier: str | None = None
    username: str | None = None
    password: str
