from typing import Union

from fastapi import FastAPI
from docx2pdf import convert

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/convert/format/{format}")
def converter(format: str, q: Union[str, None] = None):
    convert("./input.docx")
    return {"format": format, "q": q}