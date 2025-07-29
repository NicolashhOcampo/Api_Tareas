from datetime import datetime
from sqlmodel import SQLModel, Field

class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = ""
    content: str
    update_at: datetime = Field(index=True)