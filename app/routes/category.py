from fastapi import APIRouter
from pydantic import BaseModel
from db import Session, engine
from crud.category import create_category_crud, delete_category_crud, get_categories_crud, get_category_by_id_crud, update_category_crud

category_router = APIRouter(prefix="/categories", tags=["categories"])

class CategoryCreate(BaseModel):
    name: str


@category_router.get("/")
async def get_categories(limit: int = 10, offset: int = 0):
    with Session(engine) as session:
        categories = get_categories_crud(session, limit=limit, offset=offset)
        return categories
    
@category_router.get("/{category_id}")
async def get_category(category_id: int):
    with Session(engine) as session:
        category = get_category_by_id_crud(session, category_id)
        return category if category else {"message": "Category not found"}

@category_router.post("/")
async def create_category(category: CategoryCreate):

    with Session(engine) as session:
        new_category = create_category_crud(session, category.name)
        return new_category
    
@category_router.patch("/{category_id}")
async def update_category(category_id: int, category: CategoryCreate):

    with Session(engine) as session:
        updated_category = update_category_crud(session, category_id, category.name)
        return updated_category if updated_category else {"message": "Category not found"}
    
@category_router.delete("/{category_id}")
async def delete_category(category_id: int):
    with Session(engine) as session:
        deleted_category = delete_category_crud(session, category_id)
        return deleted_category if deleted_category else {"message": "Category not found"}
