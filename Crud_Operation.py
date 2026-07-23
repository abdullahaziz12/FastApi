from fastapi import FastAPI
from pydantic import  BaseModel
app=FastAPI()
my_data=[]
class Todo(BaseModel):
    id:int
    title:str
    completed:bool=False
@app.put("/todos")
def create_todo(todo:Todo):
    my_data.append(todo)
    return {"message":"todo added"}
@app.get("/todos")
def get_todos():
    return my_data
@app.get("/todos/{todo_id}")
def get_searched_id(todo_id:int):
    for i in my_data:
        if todo_id== i.id:
            return i
    return {"Error":"Todo Not Found"}
@app.put("/todos/{todo_id}")
def update_id(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(my_data):
        if todo.id==todo_id:
            my_data[index]=updated_todo
            return{"message":"Data Updated"}
        return {"Error":"Todo Not Found"}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,i in enumerate(my_data):
        if todo_id==i.id:
            my_data.pop(index)
            return{"message":"Todo Deleted"}
    return{"Message":"Todo Not Found"}
