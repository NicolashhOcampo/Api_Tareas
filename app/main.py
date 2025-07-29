from fastapi import FastAPI
from routes.category import category_router
from db import engine, SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


app.include_router(category_router)