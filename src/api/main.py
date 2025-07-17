import os
from beanie import init_beanie
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from src.database.models import Task
from src.api.tasks.views import tasks_router
from motor import motor_asyncio


url = os.getenv("MONGO_URL")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # print("MONGO_URL =", url)
    client = motor_asyncio.AsyncIOMotorClient(url)
    await init_beanie(client.get_database("todos"), document_models=[Task])
    yield


app = FastAPI(title="todos", lifespan=lifespan)
app.include_router(tasks_router)
