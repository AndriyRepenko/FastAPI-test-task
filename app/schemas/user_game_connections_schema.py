from typing import List
from .game_schema import GameBase
from .user_schema import UserBase, UserName


class UserGamesList(UserBase):
    games: List[GameBase]


class GamesUsersList(GameBase):
    users: List[UserName]
