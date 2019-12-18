from fastapi import FastAPI
from mangum import Mangum

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

app = FastAPI(openapi_prefix="/dev")


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.post("/something")
async def trololo(item: Item):
    return item.dict()

handler = Mangum(app)