from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field


class TaskIn(BaseModel):
    title: str
    description: str


class TaskDB(TaskIn):
    id: str = Field(alias="_id")


class TaskOut(BaseModel):
    id: Annotated[str, BeforeValidator(str), Field(alias="_id")]
    title: str
    description: str
    # model_config = ConfigDict(arbitrary_types_allowed=True)
