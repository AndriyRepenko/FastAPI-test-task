# FastAPI Test Task
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://github.com/tiangolo/fastapi)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://github.com/postgres/postgres)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/docker)

Test task project create using FastAPI + PostgreSQL + SQLAlchemy + Docker

## Setup

```
    git init
```

```
    git clone https://github.com/AndriyRepenko/FastAPI-test-task.git
```

create .env file

```
    POSTGRES_HOST='db' #don't change this field
    POSTGRES_USER='postgres user'
    POSTGRES_PASSWORD='postgres password'
    POSTGRES_DB='postgres_db'
```

run docker-compose with detach and build modes

```
    docker-compose up --build --detach
```