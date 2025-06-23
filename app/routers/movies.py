# app/routers/movies.py

from fastapi import APIRouter
from ..services import tmdb_service # Importamos nosso novo serviço

# APIRouter funciona como um "mini-FastAPI"
router = APIRouter()

@router.get("/popular")
async def get_popular_movies_route():
    """
    Endpoint para buscar os filmes populares do TMDB.
    """
    # A lógica do endpoint é simplesmente chamar nosso serviço
    movies = await tmdb_service.get_popular_movies()
    return movies