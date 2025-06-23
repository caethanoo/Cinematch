# app/models/user.py

from sqlalchemy import Column, Integer, String, Boolean
from ..db.database import Base # Importamos a Base que criamos

# Nosso modelo de Usuário que representa a tabela 'users' no banco
class User(Base):
    __tablename__ = "users" # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)