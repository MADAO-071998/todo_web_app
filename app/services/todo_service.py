from typing import List
from app.schemas.todo import Todo, TodoCreate

todos: List[Todo] = []
counter = 1

def create_todo(todo: TodoCreate) -> Todo:
  global counter
  new_todo = Todo(id=counter, **todo.model_dump())
  todos.append(new_todo)
  counter += 1
  return new_todo


def get_all_todos() -> List[Todo]:
  return todos