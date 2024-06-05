from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.todos_route import todos_router
import app.database as db


# The first part of the function, before the yield, will
# be executed before the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    db.create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="FASTAPI TODO")

app.include_router(todos_router)

# @app.on_event("startup")
# def startup():
#     md.create_db_and_tables()

@app.get("/")
def read_root():
    return {"App": "The TODO App Dockerized"}
