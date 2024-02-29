from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from typing import Union
from gemini_personhire_nonmarketing import personhire_nonmarketing_response
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}

desc = "This api analyses  articles  about personhire_nonmarketings achieved by a company and extracts the following information.\
    'Company Name', 'Company Domain Name', 'New Hire', 'Job title', 'Previous Workplace', 'Aim of Company with New Hire', 'Geography'."
@app.post("/api/personhire_nonmarketing:/", response_class=PlainTextResponse, description=desc)
def personhire_nonmarketing(input):
    return personhire_nonmarketing_response(input)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)