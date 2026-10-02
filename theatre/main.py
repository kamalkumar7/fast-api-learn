from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database table created")
    yield
    # shutdown: cleanup here
    print("Shutting down the app here")


app = FastAPI(
    title="Theatre Reviews API",
    description="Theatre reviews API for Delhi Theathres",
    lifespan=lifespan,
)
