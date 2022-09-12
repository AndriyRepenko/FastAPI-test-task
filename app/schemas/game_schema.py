from pydantic import BaseModel, Field

from typing import Optional


class GameBase(BaseModel):
    name: Optional[str] = Field(alias='game_name')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class GameCreate(GameBase):
    name: str


class GameUpdate(GameBase):
    pass


class Game(GameBase):
    id: int
