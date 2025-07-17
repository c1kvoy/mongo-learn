from datetime import datetime
from beanie import Document
from pydantic import Field


class Task(Document):
    title: str
    description: str
    created_at: str = str(datetime.timestamp(datetime.now()))
    updated_at: str = str(datetime.timestamp(datetime.now()))
    active: bool = False

    class Settings:
        name = "tasks"
