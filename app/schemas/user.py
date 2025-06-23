# app/schemas/user.py

from pydantic import BaseModel, EmailStr

# Schema para a criação de um usuário (o que esperamos receber na requisição)
class UserCreate(BaseModel):
    email: EmailStr # Pydantic já valida se o formato do email é válido
    password: str

# Schema para a leitura de um usuário 
class UserPublic(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True # Antigamente era orm_mode = True