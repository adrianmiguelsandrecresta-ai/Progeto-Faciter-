# Faciter — Projeto Integrador

## Problema
Facilitar a jornada de pessoas que procuram imóveis, centralizando consulta e gestão em uma única aplicação.

## Solução
A Faciter possui frontend web, API REST própria, banco relacional, autenticação JWT, CRUD de imóveis e integração externa de clima.

## Tecnologias
- Frontend: HTML, CSS e JavaScript
- Backend: Python + FastAPI
- Banco: SQLite (pode ser migrado para PostgreSQL)
- ORM: SQLAlchemy
- Testes: Pytest
- Documentação: Swagger/OpenAPI do FastAPI
- API externa: Open-Meteo

## Executar backend
1. Entre em `backend`.
2. Crie um ambiente virtual.
3. Instale `pip install -r requirements.txt`.
4. Copie `.env.example` para `.env` e altere a chave JWT.
5. Execute `uvicorn app.main:app --reload`.
6. Acesse `/docs` para Swagger.

## Executar frontend
Abra `frontend/index.html` no navegador. Para evitar limitações do navegador, é recomendado usar um servidor local, por exemplo `python -m http.server 5500` dentro de `frontend`.

## Testes
Dentro de `backend`: `pytest -q`.

## Segurança
Senhas são armazenadas com PBKDF2-HMAC-SHA256, nunca em texto puro. O token JWT utiliza variável de ambiente. O frontend não acessa o banco diretamente.

## IA
A IA pode ser declarada na documentação final do grupo. Informem ferramenta/modelo, tarefas realizadas, dificuldades, erros encontrados, correções e contribuição para o desenvolvimento.
