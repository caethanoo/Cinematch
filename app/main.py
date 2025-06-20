from fastapi import FastAPI

app = FastAPI()
# - usando o método GET (geralmente usado para buscar dados)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}