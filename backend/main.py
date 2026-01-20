from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory storage for simplicity
fake_db: List[Todo] = []

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return fake_db

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    fake_db.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: Todo):
    for idx, t in enumerate(fake_db):
        if t.id == todo_id:
            fake_db[idx] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, t in enumerate(fake_db):
        if t.id == todo_id:
            del fake_db[idx]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Todo not found")
