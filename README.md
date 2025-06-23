# 🎬 CineMatch


CineMatch é uma aplicação full-stack projetada para ajudar você e seus amigos a encontrarem o filme perfeito para assistir juntos. Usando um sistema de "swipe" interativo, similar ao Tinder, os usuários podem curtir ou dispensar filmes, e o CineMatch revela os "matches" em comum!

##  STATUS DO PROJETO

🚧 **Projeto em Andamento** 🚧

Este projeto está sendo ativamente desenvolvido como parte de um estudo prático de desenvolvimento full-stack. As funcionalidades estão sendo implementadas gradualmente.

## 🚀 Tecnologias Utilizadas

Este projeto é dividido em duas partes principais: o Backend e o Frontend.

### Backend
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Banco de Dados:** SQLAlchemy com SQLite (para desenvolvimento)
- **Validação de Dados:** Pydantic
- **Autenticação:** JWT (JSON Web Tokens) e Passlib para hashing de senhas
- **Comunicação com APIs:** HTTPX

### Frontend (Planejado)
- **Linguagem:** JavaScript/TypeScript
- **Framework/Biblioteca:** React
- **Estilização:** a definir (ex: Styled Components, TailwindCSS)
- **Comunicação com Backend:** Axios

## ⚙️ Como Rodar o Projeto Localmente

Para executar o backend localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/cinematch.git](https://github.com/SEU-USUARIO/cinematch.git)
    cd cinematch
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *No Windows, o comando para ativar é `venv\Scripts\activate`*

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    - Copie o arquivo `.env.example` para um novo arquivo chamado `.env`.
    - `cp .env.example .env`
    - Abra o arquivo `.env` e preencha a variável `TMDB_API_KEY` com a sua chave da API do The Movie Database.

5.  **Execute o servidor:**
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **Acesse a aplicação:**
    - A API estará disponível em `http://127.0.0.1:8000`.
    - A documentação interativa estará em `http://127.0.0.1:8000/docs`.

## 🗺️ Roadmap e Funcionalidades

### Funcionalidades Planejadas
- [x] Cadastro de Usuários com senha segura
- [ ] Login de Usuários com autenticação JWT
- [ ] Rotas protegidas acessíveis apenas para usuários logados
- [ ] Integração com a API do TMDB para buscar filmes
- [ ] Sistema de "Swipe" (like/dislike) de filmes
- [ ] Lógica para identificar "matches" entre usuários
- [ ] Listagem de filmes favoritados e matches

## ✍️ Autores

- Brennda Caethano - ([@caethanoo](https://github.com/caethanoo))
- 
---
> Projeto desenvolvido como parte de um bootcamp de aprendizado intensivo.