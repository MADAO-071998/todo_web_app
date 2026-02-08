from fastapi import APIRouter
from app.schemas.todo import Todo, TodoCreate
from app.services.todo_service import create_todo, get_all_todos, get_todo_by_id
from typing import List
from fastapi import HTTPException

router = APIRouter()

@router.get("/")
def root():
  return {"status": "To-Do API running"}

@router.get("/health")
def check_health():
  return {"status": "ok"}

@router.post("/todos", response_model=Todo)
def create(todo: TodoCreate):
  return create_todo(todo)

@router.get("/todos", response_model=List[Todo])
def get_all():
  return get_all_todos()

@router.get("/todos/{todo_id}", response_model=Todo)
def get_one(todo_id: int):
  todo = get_todo_by_id(todo_id)
  if not todo:
    raise HTTPException(status_code=404, detail="Todo not found")
  return todo