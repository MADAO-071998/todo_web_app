from fastapi import APIRouter
from app.schemas.todo import Todo, TodoCreate
from app.services.todo_service import create_todo, get_all_todos
from typing import List

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