from fastapi import FastAPI

app = FastAPI()


@app.get("/tree")
def tree():
    return {"favourite_tree": "oak"}
