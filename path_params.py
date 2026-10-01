#Path Parameteres
from fastapi import FastAPI, Path
import json


def load_data():
    with open("data.json", "r") as d:
        data = json.load(d)
    return data

app = FastAPI()

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the Patient', example='P001')):
    # load data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error': 'patient not found'}

