from sqlmodel import Session, select
from models.model import Category

def get_categories_crud(session: Session, limit: int = 10, offset: int = 0):
    statement = select(Category).offset(offset).limit(limit)
    return session.exec(statement).all()

def get_category_by_id_crud(session: Session, category_id: int):
    return session.get(Category, category_id)

def create_category_crud(session: Session, name: str):
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()
    session.refresh(new_category)
    return new_category

def update_category_crud(session: Session, id: int, name: str):
    category = session.get(Category, id)
    if not category:
        return None
    category.name = name
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def delete_category_crud(session: Session, id: int):
    category = session.get(Category, id)
    if not category:
        return None
    session.delete(category)
    session.commit()
    return category