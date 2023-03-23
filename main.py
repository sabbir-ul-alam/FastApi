from fastapi import FastAPI, Path
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
def get_student(student_id : int = Path(description= "The ID of the student you want to view",gt=0,lt=3)):
    return {
        json.dumps(students[student_id],indent=4)
    }

