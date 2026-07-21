from fastapi import FastAPI
app = FastAPI()
#Home Page
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
#Users Page Dynamic Routing 
@app.get("/users/{user_id}")
def users(user_id):
    return{
        "Userid":user_id
    }
#Test Page Validation
@app.get("/test/{Test_id}")
def testpage(Test_id:int):
    return {
        "Test ID":Test_id
    }