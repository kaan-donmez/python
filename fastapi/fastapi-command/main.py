import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hi, Welcome to FastAPI!"}

@app.get("/about")
def about():
    return {"message": "About"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)