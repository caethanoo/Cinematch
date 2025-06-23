# app/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco de dados (lembra do arquivo .env?)
# "sqlite:///./cinematch.db" indica que usaremos o SQLite e o arquivo estará na raiz do projeto.
SQLALCHEMY_DATABASE_URL = "sqlite:///./cinematch.db"

# O "engine" é o ponto de entrada para o banco de dados.
# O argumento connect_args é necessário apenas para o SQLite.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cada instância de SessionLocal será uma sessão (uma "conversa") com o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Usaremos esta Base para criar cada um dos nossos modelos (tabelas) do banco.
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()