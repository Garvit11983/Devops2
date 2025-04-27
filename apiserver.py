from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}

@app.get("/subtract/{num1}/{num2}")
def subtract(num1: int, num2: int):
    return {"result": num1 - num2}

@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    return {"result": num1 * num2}

# Ensure uvicorn is started in the correct place
if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run("apiserver:app", host="0.0.0.0", port=8002, reload=True, log_level="debug")
    print("Server started on http://localhost:8002")
