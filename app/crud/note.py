from datetime import datetime
from sqlmodel import Session, select
from models.note import Note

def get_notes_crud(session: Session, limit: int = 10, offset: int = 0):
    statement = select(Note).offset(offset).limit(limit)
    return session.exec(statement).all()

def get_note_by_id_crud(session: Session, note_id: int):
    return session.get(Note, note_id)

def create_note_crud(session: Session, title: str, content: str, category_id: int | None = None):
    new_note = Note(title=title, content=content, category_id=category_id, update_at=datetime.now())
    session.add(new_note)
    session.commit()
    session.refresh(new_note)
    return new_note