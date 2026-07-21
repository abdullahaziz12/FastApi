from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def homepage():
    return {
        "message":"Hello this is home page"
    }
#About Page
@app.get("/about")
def about():
    return{
        "message":"this is About Page"
    }
@app.get("/users")
def users():
    return{
        "message":["Abdullah","Aziz"],
        "age":22
    }
@app.get("/test")
def testpage():
    return {
        "message":"Hello this is test page"
    }
