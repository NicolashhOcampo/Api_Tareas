from fastapi import APIRouter
from pydantic import BaseModel
from crud.note import get_notes_crud, get_note_by_id_crud, create_note_crud
from db import Session, engine

note_router = APIRouter(prefix="/notes", tags=["notes"])

class NoteCreate(BaseModel):
    title: str
    content: str
    category_id: int | None = None
    
    
@note_router.get("/")
async def get_notes(limit: int = 10, offset: int = 0):
    with Session(engine) as session:
        notes = get_notes_crud(session, limit=limit, offset=offset)
        return notes
    
@note_router.get("/{note_id}")
async def get_note(note_id: int):
    with Session(engine) as session:
        note = get_note_by_id_crud(session, note_id)
        return note if note else {"message": "Note not found"}

@note_router.post("/")
async def create_note(note: NoteCreate):
    with Session(engine) as session:
        new_note = create_note_crud(session, title=note.title, content=note.content, category_id=note.category_id)
        return new_note