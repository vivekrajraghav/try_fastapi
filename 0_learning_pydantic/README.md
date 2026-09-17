![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.x-e92063?logo=pydantic&logoColor=white)
![uv](https://img.shields.io/badge/uv-Fast-purple)

# Learning Pydantic

This repository tracks my progress in learning and implementing **Pydantic** for data validation and settings management in Python. It serves as a personal reference for revisiting core concepts and code snippets.

## Why to use Pydantic?

Pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. Key benefits include:

*   **Data Validation:** Guarantees that the data structures match the defined schema and fails loudly when they do not.
*   **Automatic Type Coercion:** Intelligently converts input types (e.g., parsing the string `"123"` into the integer `123`) when safe to do so.
*   **IDE Integration:** Built on standard Python type hints (`typing`), meaning excellent autocompletion and linting in editors like VS Code or PyCharm.
*   **Less Boilerplate:** Eliminates the need for custom `__init__` methods and manual type-checking logic.
*   **Deeply Nested Structures:** Easily validates complex, nested dictionaries and lists natively.

## Tech Stack

*   **Language:** Python 3.11
*   **Package Manager:** [uv](https://github.com/astral-sh/uv) (for fast dependency resolution and environment management)
*   **Core Library:** Pydantic

## Code Example: Student Data Validation

Below is a core example demonstrating how to define a data model using `BaseModel` and validate a dictionary of student information.

```python
from pydantic import BaseModel
from typing import List, Dict

class Students(BaseModel):
    name: str
    roll_no: int
    total_marks: int
    passed: bool
    subjects: List[str]
    sub_marks: Dict[str, int] # Dict[key, value]
    contact_details: dict[str, str]

def update_details(student: Students):
    print(student.name)
    print(student.roll_no)
    print(student.contact_details)
    print(student.subjects)
    print(student.sub_marks)
    print(student.total_marks)
    print(student.passed)

student_info = {
    "name": "Vivek",
    "roll_no": 123456,
    "subjects": ["English", "Physics", "Chemistry"],
    "sub_marks": {"English": 75, "Physics": 80, "Chemistry": 70},
    "total_marks": 225,
    "passed": True,
    "contact_details": {"mobile": "1234567890", "email": "abc@gmail.com"}
}

student1 = Students(**student_info)
update_details(student1)

```

## Running the Code Locally

You can set up the environment and run the code locally using `uv`:

```bash
# 1. Create a virtual environment using Python 3.11
uv venv --python 3.11

# 2. Activate the virtual environment
# On Windows:
# .venv\Scripts\activate

# 3. Install Pydantic into the virtual environment
uv pip install pydantic

# 4. Run the script (assuming the file is named main.py)
python main.py

```