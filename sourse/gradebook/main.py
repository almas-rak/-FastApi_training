from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База Создана")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

