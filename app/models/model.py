from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    notes: list["Note"] = Relationship(back_populates="user")
    categories: list["Category"] = Relationship(back_populates="user")

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    notes: list["Note"] = Relationship(back_populates="category")
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    user: User | None = Relationship(back_populates="categories")

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = ""
    content: str
    update_at: datetime = Field(index=True)
    
    category_id: int | None = Field(default=None, foreign_key="category.id", ondelete="SET NULL")
    category: Category | None = Relationship(back_populates="notes")
    
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    user: User | None = Relationship(back_populates="notes")
    
