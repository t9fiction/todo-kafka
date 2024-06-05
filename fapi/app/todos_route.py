from fastapi import APIRouter
from sqlmodel import Session, select
# from fastapi.exceptions import HTTPException
from app.engine_file import engine
from app.models import Todo, TodoPost
from fastapi import HTTPException

todos_router = APIRouter(
    prefix="/todos",
    tags=['todos']
)

@todos_router.get("/{id}")
def todo_id(id):
    return {"message": f"todo {id}"}


@todos_router.get("/")
def read_todos():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return todos

@todos_router.post("/")
def create_todo(todo: Todo):
    with Session(engine) as session:
        todo_to_create = Todo.model_validate(todo)
        todo_id = session.exec(select(Todo).where(Todo.id == todo_to_create.id))
        if todo_id.first() is not None:
            raise HTTPException(status_code=404, detail="ID is not unique")
        
        todo_query = select(Todo).where(Todo.name == todo_to_create.name)
        todo_first = session.exec(todo_query).first()
        print(todo_first)

        if todo_first is not None:
            raise HTTPException(status_code=404, detail="Todo already exists.")
        
        print(todo_to_create)
        session.add(todo_to_create)
        session.commit()
        session.refresh(todo_to_create)
        return todo_to_create
    
@todos_router.put("/{id}")
def update_todo(id, todo: TodoPost):
    with Session(engine) as session:
        todo_to_update = session.get(Todo, id)
        if todo_to_update is None:
            raise HTTPException(status_code=404, detail="Todo not found.")
        todo_to_update.name = todo.name
        todo_to_update.content = todo.content
        session.commit()
        session.refresh(todo_to_update)
        return todo_to_update
    
@todos_router.delete("/{id}")
def delete_todo(id):
    with Session(engine) as session:
        todo_to_delete = session.get(Todo, id)
        if todo_to_delete is None:
            raise HTTPException(status_code=404, detail="Todo not found.")
        session.delete(todo_to_delete)
        session.commit()
        return {"message": "Todo deleted"}

