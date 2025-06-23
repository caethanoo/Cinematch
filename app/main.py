# app/main.py

from fastapi import FastAPI
from .db.database import engine
from .models import user 
# Importamos o nosso novo router de filmes
from .routers import movies

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluímos o router de filmes na nossa aplicação principal
# prefix="/movies" significa que todas as rotas em movies.router começarão com /movies
# tags=["Movies"] agrupa os endpoints na documentação interativa
app.include_router(movies.router, prefix="/movies", tags=["Movies"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao CineMatch! Dia 3!"}