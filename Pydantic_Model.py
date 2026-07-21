from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    name:str
    age:int
    email:str
# Simple Pydantic Validation
@app.post("/Users")
def Users(new_user:User):
    return {
        "message":"User Created",
        "data":new_user
    }
# Nested Pydantic Validation
class Address(BaseModel):
    city:str
    postalcode:int
class Nested_User(BaseModel):
    name:str
    age:int
    email:str
    address:Address
@app.post("/New_Users")
def Users(New_user:Nested_User):
    return {
        "message":"User Created",
        "data":New_user
    }