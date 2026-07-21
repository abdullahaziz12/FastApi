from fastapi import FastAPI
from pydantic import BaseModel
class Users(BaseModel):
    name:str
    age:int
app=FastAPI()
# Post Api With Data Validation
@app.post("/Users")
def Create_user(name:str,age:int):
    return {
        "Message":"User Created",
        "Data": {
            "name":name,
            "age":age
        }
            
    }
#Without Data Validation
@app.post("/newUsers")
def Create_user(users:dict):
    return {
        "Message":"User Created",
        "Data": users
            
    }
#Data Validation With Pydantic
@app.post("/Users-pydantic")
def Users_pydantic(user:Users):
    return{
        "message":"User Created",
        "data":user
    }