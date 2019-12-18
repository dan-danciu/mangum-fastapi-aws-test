from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(openapi_prefix="/dev")


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/something")
async def trololo():
    return {"message": "Here you go"}

handler = Mangum(app)