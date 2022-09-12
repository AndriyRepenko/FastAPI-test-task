from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

from app.database import Base


class Connections(Base):
    __tablename__ = 'connections'

    user_id = Column(ForeignKey('user.id'), primary_key=True)
    game_id = Column(ForeignKey('game.id'), primary_key=True)
    game = relationship("Game", back_populates="users")
    user = relationship("User", back_populates="games")

    # proxies
    game_name = association_proxy(target_collection='game', attr='name')
    user_name = association_proxy(target_collection='user', attr='name')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)
    games = relationship('Connections', back_populates='user')


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    users = relationship('Connections', back_populates='game')
