from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

@app.post("/app/{item}",status_code=201)
async def read_item(item:str):
    return {"message":f"hello {name}"}
