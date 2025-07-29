from fastapi import FastAPI
from routes.category import category_router
from routes.note import note_router
from db import create_db_and_tables

app = FastAPI()

create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


app.include_router(category_router)
app.include_router(note_router)