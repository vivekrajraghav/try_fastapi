from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def intro():
    return {"Hello, I'm Vivek"}

@app.get("/about")
def moreinfo():
    return {"I'm a MTech Student"}

