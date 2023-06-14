# __author__ = 'Ravi Bhavsar'
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_active: bool

@app.get("/")
def index():
    return {"title" : "Hello coder follower, please like this video!"}

@app.post("/items/")
async def create_item(item: Item):
    if item.name is None or item.name == '':
        raise HTTPException(status_code=400, detail="Invalid item data")
    return {"message": "Item created successfully", "item": item}
