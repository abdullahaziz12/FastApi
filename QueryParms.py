from fastapi import FastAPI
app=FastAPI()
@app.get("/users")
def users_page(name):
    return f"My name is {name}"
#Default Values
@app.get("/items")
def items_limit(limit:int =40):
    return {"items_Limit":limit}
#Multiple Query Parms
@app.get("/product")
def product(name:str=None,price:float=0):
    return {
        "name":name,
        "price":price
    }