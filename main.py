from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}


from config import db_url, tmdb_key

print(db_url)
print(tmdb_key)
