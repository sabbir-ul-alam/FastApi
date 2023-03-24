from fastapi import FastAPI, Path
import json
from typing import Optional
app = FastAPI()

students = {
    1: {
        "name" : "Sabbir",
        "age"  : 28,
        "class" : "Bsc"
    }
}


@app.get("/")
def home():
    return {
        "name": "First Data"
    }
@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description= "The ID of the student you want to view",gt=0,lt=3)):
    return {
        json.dumps(students[student_id],indent=4)
    }

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return json.dumps(students[student_id])
        return {
            "Data" : "Not found"
        }

