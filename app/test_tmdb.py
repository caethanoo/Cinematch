import requests

API_KEY = 'a311e6a736ad8ed030dde84fbb5fc5cc'
base_url = 'https://api.themoviedb.org/3'

# Função para pegar filmes populares
def get_popular_movies():
    url = f"{base_url}/movie/popular"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR',
        'page': 1
    }
    response = requests.get(url, params=params)
    return response.json()

# Função para pegar gêneros
def get_movie_genres():
    url = f"{base_url}/genre/movie/list"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    popular_movies = get_popular_movies()
    genres = get_movie_genres()

    print("Gêneros disponíveis:")
    for genre in genres['genres']:
        print(f"{genre['id']}: {genre['name']}")

    print("\nFilmes populares:")
    for movie in popular_movies['results'][:5]:
        print(f"- {movie['title']} (Gêneros IDs: {movie['genre_ids']})")
