"""Minimal FastAPI starter scaffold for the assignment.

Endpoints provided (in-memory store):
- GET /items
- GET /items/{item_id}
- POST /items
- PUT /items/{item_id}
- DELETE /items/{item_id}

Run during development with:
    uvicorn starter-code:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from uuid import uuid4

app = FastAPI(title="Intro FastAPI CRUD")


class Item(BaseModel):
    name: str
    description: str | None = None


# In-memory store: id -> Item
STORE: Dict[str, Item] = {}


@app.get("/items")
def list_items():
    return [{"id": _id, **item.dict()} for _id, item in STORE.items()]


@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = STORE.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **item.dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    item_id = str(uuid4())
    STORE[item_id] = item
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id not in STORE:
        raise HTTPException(status_code=404, detail="Item not found")
    STORE[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    if item_id not in STORE:
        raise HTTPException(status_code=404, detail="Item not found")
    del STORE[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
