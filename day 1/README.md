# FastAPI Day 1: The Basics

This repository contains my very first steps in learning FastAPI. It is a simple, lightweight API that serves as a digital introduction, documenting my journey.

## 🛠️ Tech Stack & Tools

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=flat&logo=fastapi&logoColor=white) ![uv](https://img.shields.io/badge/uv-Package_Manager-7a2fe5?style=flat) ![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-c53e37?style=flat)

## 📝 The Code (`main.py`)
This is the foundational code for the API. 
```python
from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

# Root endpoint
@app.get("/")
def intro():
    return {"message": "Hello, I'm Vivek"}

# About endpoint
@app.get("/about")
def moreinfo():
    return {"message": "I'm an MTech Student"}

```

## 🚀 How to Run Locally

### 1. Install Dependencies

Instead of standard `pip`, this project uses `uv` to prevent global storage inflation and version conflicts. Make sure `uv` is installed, then run:

```bash
uv add fastapi uvicorn pydantic

```

### 2. Start the Server

To launch the API, use the Uvicorn server. The `--reload` flag ensures the server automatically restarts whenever the code is saved.

```bash
uvicorn main:app --reload

```

### 3. View the API

Once the server is running, open a web browser and visit:

* 🏠 **Root:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/?utm_source=gemini)
* ℹ️ **About:** [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about?utm_source=gemini)

### 4. 🪄 Automatic API Documentation

FastAPI automatically generates beautiful, interactive documentation based on your code. You don't have to write any extra configuration for this! Once your server is running, you can explore and test your API directly from the browser:

* 📄 **Swagger UI (Interactive testing):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs?utm_source=gemini)
* 📑 **ReDoc (Clean, static reading):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc?utm_source=gemini)

## 📖 Key Learnings from Day 1

1. **Routing:** Using decorators like `@app.get("/")` to map URLs to specific Python functions.
2. **Data Serialization:** APIs communicate in JSON, which means Python functions should return dictionaries, not sets.
3. **CLI Execution:** Using the exact `uvicorn <filename>:<app_variable>` syntax to boot up the application.
4. **Virtual Environments:** Utilizing `uv` to automatically manage isolated project environments and avoid system-wide dependency conflicts.
5. **Auto-Docs:** FastAPI automatically creates OpenAPI-compliant documentation available at the `/docs` and `/redoc` endpoints.
