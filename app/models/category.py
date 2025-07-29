from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str