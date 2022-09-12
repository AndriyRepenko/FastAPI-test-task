from pydantic import BaseModel

from typing import Optional


class ConnectionBase(BaseModel):
    user_id: Optional[int] = None
    game_id: Optional[int] = None


class ConnectionCreate(ConnectionBase):
    user_id: int
    game_id: int

    class Config:
        orm_mode = True


class ConnectionUpdate(ConnectionBase):
    pass
