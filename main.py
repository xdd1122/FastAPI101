from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello2")
def read_root():
    return {"Hello": "World, again"}

@app.get("/hello3")
def read_root():
    return {"Hello": "World, for the third time"}