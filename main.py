from fastapi import FastAPI
import json

def load_data():
    with open('data.json', "r") as d:
        data = json.load(d)
    return data

app = FastAPI()

@app.get("/") # End Point
def home():
    return {"message": "My First API is working"}

@app.get("/about")
def about():
    return {"name": "Muhammad Jamshaid"}

@app.get("/view")
def view_data():
    data = load_data()
    return data