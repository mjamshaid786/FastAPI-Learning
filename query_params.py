from fastapi import FastAPI, Query, HTTPException

import json

app = FastAPI()

def load_data():
    with open('data.json', 'r') as d:
        data = json.load(d)
    return data

# data = load_data()
# for patient_id, details in data.items():
#     if details["city"] == "Pune":
#         print(f"Patient ID: {patient_id}\nDetails: {details}")

@app.get('/patient')
def view_patient(city_name: str = Query(..., description='City Name', example='Lahore')):
    # load data
    data = load_data()
    results = {}
    for patient_id, details in data.items():
        if details['city'].lower() == city_name.strip().lower():
            results[patient_id] = details
    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No patient found in {city_name}"
        )
    return results

