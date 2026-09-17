from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def intro():
    return {"message":"Hello, I'm Vivek"}

@app.get("/about")
def moreinfo():
    return {"message":"I'm a MTech Student"}

