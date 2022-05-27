from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def tree():
    tree_name = os.environ.get("TREE", "pine")
    return {"favourite_tree": tree_name}
