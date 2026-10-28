from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import auth, imoveis, clima

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Faciter API", version="1.0.0", description="API da plataforma Faciter")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router)
app.include_router(imoveis.router)
app.include_router(clima.router)

@app.get("/", tags=["Sistema"])
def root(): return {"mensagem": "Faciter API funcionando"}

@app.get("/health", tags=["Sistema"])
def health(): return {"status": "ok"}
