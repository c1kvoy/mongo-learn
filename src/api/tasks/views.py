from fastapi import Body
from fastapi.routing import APIRouter

from src.api.tasks.schemas import TaskIn
from src.database.models import Task

tasks_router = APIRouter(prefix="/tasks")


@tasks_router.get(
    "/", response_model=list[str], response_model_by_alias=True
)  # список Task
async def get_all_tasks():
    tasks = await Task.find_all().to_list()
    return [str(task.id) for task in tasks]


@tasks_router.post("/", response_model=Task, response_model_by_alias=True)
async def create_task(task: TaskIn = Body(...)):

    t = await Task(**task.model_dump()).insert()
    return t


# @tasks_router.post("/", response_model_by_alias=True)
# async def create_task(task: TaskIn):
#     try:
#         inserted = await tasks_collection.insert_one(task.model_dump())
#         doc = await tasks_collection.find_one({"_id": inserted.inserted_id})
#         return TaskOut.model_validate(doc, from_attributes=True)
#     except Exception as e:
#         print(e)


# @tasks_router.get("/", response_model=list[TaskOut])
# async def get_all_task():
#     tasks = await tasks_collection.find().to_list()
#     return [TaskOut.model_validate(task) for task in tasks]


# @tasks_router.patch("/")
# async def update_task(task: TaskDB):
#     obj_id = objectid.ObjectId(task.id)
#     updated = await tasks_collection.find_one_and_update(
#         {"_id": obj_id}, {"$set": task.model_dump()}
#     )
#     return TaskOut.model_validate(updated)
