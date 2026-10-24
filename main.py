from fastapi import FastAPI
app = FastAPI()
@app.get("/sahib")
def sahib():
    return "hii i am sahibjot singh"
@app.get("/coding")
def coding():
    return "this is my first api"