from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from typing import Union

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}



if __name__ == "__main__":
    uvicorn.run(app, port=8000)
