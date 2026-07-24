from fastapi import FastAPI
from pydantic import BaseModel
class Calculator(BaseModel):
    num1:int
    num2:int
app=FastAPI()
def sum(num1:float,num2:float):
    return num1+num2
def multiply(num1:float,num2:float):
    return num1*num2
def divide(num1:float,num2:float):
    return num1/num2
def subtr(num1:float,num2:float):
    return num1-num2
@app.post("/addition")
def addition(num:Calculator):
    global total
    total=sum(num.num1,num.num2)
    return {"message": "calculated successfully", "data": total}
@app.post("/subtraction")
def subtraction(num:Calculator):
    global total
    total=subtr(num.num1,num.num2)
    return {"message": "calculated successfully", "data": total}
@app.post("/multiplication")
def multiplication(num:Calculator):
    global total
    total=multiply(num.num1,num.num2)
    return {"message": "calculated successfully", "data": total}
@app.post("/division")
def division(num:Calculator):
    global total
    if num.num1==0:
        return {"message":"Cant Divide by 0"}
    total=divide(num.num1,num.num2)
    return {"message": "calculated successfully", "data": total}
@app.get("/result")
def get_ans():
    return{"message":"Calculation answer","data":total}