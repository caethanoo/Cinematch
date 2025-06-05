from dotenv import load_dotenv
import os

load_dotenv()  # Carrega automaticamente as variáveis do .env

db_url = os.getenv("DATABASE_URL")
tmdb_key = os.getenv("TMDB_API_KEY")
