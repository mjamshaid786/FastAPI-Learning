from fastapi import FastAPI
app = FastAPI()

@app.get("/") # End Point
def home():
    return {"message": "My First API is working"}

@app.get("/about")
def about():
    return {"name": "Muhammad Jamshaid"}