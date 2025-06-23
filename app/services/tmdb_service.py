# app/services/tmdb_service.py

import httpx
import os # Usaremos para pegar a variável de ambiente
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_API_URL = "https://api.themoviedb.org/3"

async def get_popular_movies():
    """
    Busca os filmes populares da API do TMDB.
    """
    # Montamos a URL completa para o endpoint de filmes populares
    endpoint = f"{TMDB_API_URL}/movie/popular"
    # Adicionamos os parâmetros necessários, como a chave da API e o idioma
    params = {"api_key": TMDB_API_KEY, "language": "pt-BR"}

    # Usamos o httpx.AsyncClient para fazer a chamada de forma assíncrona
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(endpoint, params=params)
            # Levanta uma exceção se a resposta for um erro (4xx ou 5xx)
            response.raise_for_status() 
            # Retorna a lista de filmes que fica dentro da chave 'results' do JSON
            return response.json().get("results", [])
        except httpx.HTTPStatusError as e:
            # Em caso de erro na chamada, podemos logar e retornar uma lista vazia
            print(f"Erro ao buscar filmes populares: {e}")
            return []
        except htt.RequestError as e:
            print(f"Erro de requisição ao buscar filmes: {e}")
            return []