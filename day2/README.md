# FastAPI Day 2: Path Parameters, Query Parameters & Error Handling

This repository contains my Day 2 progress with FastAPI. Building upon the basic endpoints from Day 1, this project introduces dynamic routing, user input validation, and proper error handling by serving student data from a structured JSON dictionary.

## 🛠️ Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=flat&logo=fastapi&logoColor=white) ![uv](https://img.shields.io/badge/uv-Package_Manager-7a2fe5?style=flat) ![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-c53e37?style=flat)

## 🧠 Core Concepts Explored
This code steps beyond static text and implements several essential backend concepts:

1. **Path Parameters (`Path`)**: Used in `@app.get("/student/{student_id}")`. This allows the API to capture values directly from the URL path. By importing `Path`, the code also adds metadata (like `example="STU1001"`), which automatically populates the interactive `/docs`.
2. **Query Parameters (`Query`)**: Used in `@app.get("/sort")`. Unlike path parameters, query parameters are added to the end of a URL after a `?` (e.g., `/sort?sort_by=age&order=desc`). They are ideal for filtering or sorting data.
3. **Error Handling (`HTTPException`)**: The API now safely handles bad requests. Instead of crashing Python, it returns standard HTTP status codes like `404 Not Found` (if a student ID doesn't exist) or `400 Bad Request` (if a user tries to sort by an invalid field).
4. **Data Manipulation**: Leveraging Python's built-in `sorted()` function alongside a `lambda` key to dynamically arrange the JSON data based on the API's query inputs.

## 📝 The Code (`main.py`)

```python
from fastapi import FastAPI, Path, HTTPException, Query
import json

def load_data():
    with open("../students_data.json", 'r') as f:
        data = json.load(f)
    return data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome!"}

@app.get("/about")
def aboutweb():
    return {"message": "This is a trial API"}

@app.get("/view")
def viewdata():
    return load_data()

@app.get("/student/{student_id}")
def view_student(student_id: str = Path(..., description="Unique ID of Student", example="STU1001")):
    # Load all student data
    data = load_data()
    if student_id in data:
        return data[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found in DB")

@app.get("/sort")
def sort_students(
    sort_by: str = Query(..., description="Sort on basis of age, gpa, enrollment_year"),
    order: str = Query("asc", description="Sort in asc or desc")
):
    valid_fields = ["age", "gpa", "enrollment_year"]
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected, Please selected from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order, please select from asc or desc")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    
    # Sorts the values of the dictionary dynamically
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

```

## 🚀 API Endpoints Overview

| Method | Endpoint | Description | Example URL |
| --- | --- | --- | --- |
| **GET** | `/` | Root endpoint welcoming the user | `http://127.0.0.1:8000/` |
| **GET** | `/about` | Basic text information endpoint | `http://127.0.0.1:8000/about` |
| **GET** | `/view` | Returns the entire JSON dictionary | `http://127.0.0.1:8000/view` |
| **GET** | `/student/{id}` | Fetches a single student by their unique ID | `http://127.0.0.1:8000/student/STU1005` |
| **GET** | `/sort` | Sorts the database by specified fields | `http://127.0.0.1:8000/sort?sort_by=gpa&order=desc` |

## 💻 How to Run

1. Open your terminal inside your project directory.
2. Ensure your virtual environment is active.
3. Start the server using Uvicorn:
```bash
uvicorn main:app --reload

```
