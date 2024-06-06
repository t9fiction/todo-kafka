from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.todos_route import todos_router
import app.database as db
from aiokafka import AIOKafkaConsumer
import asyncio

async def consume(topic, bootstrap):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap,
        group_id='mygroup'
    )
    await consumer.start()
    try:
        # Ented the action to perform
        async for message in consumer:
            print(f"Received message: {message.value.decode()} on topic {message.topic}")
    finally:
        # finally stop the consumer
        await consumer.stop()
        
# The first part of the function, before the yield, will
# be executed before the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Running the Kafka todo App..")
    task = asyncio.create_task(consume('todos','broker:19092'))
    db.create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="FASTAPI with Kafka TODO App")

app.include_router(todos_router)

# @app.on_event("startup")
# def startup():
#     md.create_db_and_tables()

@app.get("/")
def read_root():
    return {"App": "The FASTAPI-TODO with Kafka"}
