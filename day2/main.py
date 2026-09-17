from fastapi import FastAPI,Path,HTTPException,Query
import json

def load_data():
    with open("../students_data.json",'r') as f:
        data=json.load(f)
    return data

app=FastAPI()
@app.get("/")
def home():
    return {"message":"Welcome!"}
@app.get("/about")
def aboutweb():
    return {"message":"This is a trial API"}
@app.get("/view")
def viewdata():
    return load_data()

@app.get("/student/{student_id}")
def view_student(student_id:str =Path(...,description="Unique ID of Student",example="STU1001")):
    #load all student data
    data=load_data()
    if student_id in data:
        return data[student_id]
    else:
        raise HTTPException(status_code=404,detail="Student not found in DB")
@app.get("/sort")
def sort_students(sort_by:str=Query(...,description="Sort on basis of age, gpa, enrollment_year",),order:str=Query("asc",description="Sort in asc or desc")):
    valid_fields=["age","gpa","enrollment_year"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field selected, Please selected from {valid_fields}")
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400,detail="Invalid order, please select from asc or desc")
    data=load_data()
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data
