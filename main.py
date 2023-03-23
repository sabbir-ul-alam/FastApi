from fastapi import FastAPI
import json
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
def get_student(student_id : int):
    return {
        json.dumps(students[student_id],indent=4)
    }

