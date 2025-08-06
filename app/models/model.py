from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    notes: list["Note"] = Relationship(back_populates="category")

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = ""
    content: str
    update_at: datetime = Field(index=True)
    category_id: int | None = Field(default=None, foreign_key="category.id", ondelete="SET NULL")
    category: Category | None = Relationship(back_populates="notes")