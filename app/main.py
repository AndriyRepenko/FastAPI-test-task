from typing import Any, List

from fastapi import FastAPI, Depends, HTTPException
from app.database import SessionLocal, engine
from sqlalchemy.orm import Session, joinedload
from app.schemas import user_schema, game_schema, connection_schema, user_game_connections_schema
from app import crud, models
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# user endpoints

@app.post("/users", response_model=user_schema.User, status_code=HTTP_201_CREATED)
def create_user(*, db: Session = Depends(get_db), user_in: user_schema.UserCreate) -> Any:
    user = crud.user.create(db=db, obj_in=user_in)
    return user


@app.get("/users/{id}", response_model=user_schema.User)
def get_user(*, db: Session = Depends(get_db), id: int) -> Any:
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return user


@app.put("/users/{id}", response_model=user_schema.User)
def update_user(*, db: Session = Depends(get_db), id: int, user_in: user_schema.UserUpdate, ) -> Any:
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = crud.user.update(db=db, db_obj=user, obj_in=user_in)
    return user


@app.delete("/users/{id}", response_model=user_schema.User)
def delete_user(*, db: Session = Depends(get_db), id: int) -> Any:
    user = crud.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = crud.user.remove(db=db, id=id)
    return user


# game endpoints

@app.post("/games", response_model=game_schema.Game, status_code=HTTP_201_CREATED)
def create_game(*, db: Session = Depends(get_db), game_in: game_schema.GameCreate) -> Any:
    game = crud.game.create(db=db, obj_in=game_in)
    return game


@app.get("/games/{id}", response_model=game_schema.Game)
def get_game(*, db: Session = Depends(get_db), id: int) -> Any:
    game = crud.game.get(db=db, id=id)
    if not game:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Game not found")
    return game


@app.put("/games/{id}", response_model=game_schema.Game)
def update_game(*, db: Session = Depends(get_db), id: int, game_in: game_schema.GameUpdate, ) -> Any:
    game = crud.game.get(db=db, id=id)
    if not game:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Game not found")
    game = crud.game.update(db=db, db_obj=game, obj_in=game_in)
    return game


@app.delete("/games/{id}", response_model=game_schema.Game)
def delete_game(*, db: Session = Depends(get_db), id: int) -> Any:
    game = crud.game.get(db=db, id=id)
    if not game:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Game not found")
    game = crud.game.remove(db=db, id=id)
    return game


# test task endpoints


@app.post("/users/games/", response_model=connection_schema.ConnectionCreate)
def connect_game(*, db: Session = Depends(get_db), connect_in: connection_schema.ConnectionCreate) -> Any:
    connect = crud.action.create(db=db, obj_in=connect_in)
    return connect


@app.get("/users/{id}/games/", response_model=user_game_connections_schema.UserGamesList)
def get_user_games(id: int, db: Session = Depends(get_db)):
    user_games = db.query(models.User).options(joinedload(models.User.games)).where(models.User.id == id).one()
    return user_games


@app.get("/games/", response_model=List[user_game_connections_schema.GamesUsersList])
def get_games_users(db: Session = Depends(get_db)):
    games_users = db.query(models.Game).options(joinedload(models.Game.users)).all()
    return games_users
