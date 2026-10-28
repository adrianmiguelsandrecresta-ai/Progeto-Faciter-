from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Usuario
from ..schemas import UsuarioCadastro, Login, UsuarioSaida, Token
from ..security import hash_password, verify_password, create_token
from ..dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/cadastro", response_model=UsuarioSaida, status_code=201)
def cadastro(data: UsuarioCadastro, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == data.email).first():
        raise HTTPException(409, "Email já cadastrado")
    user = Usuario(nome=data.nome, email=data.email, senha_hash=hash_password(data.senha), tipo=data.tipo)
    db.add(user); db.commit(); db.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(data: Login, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == data.email).first()
    if not user or not verify_password(data.senha, user.senha_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Email ou senha inválidos")
    return {"access_token": create_token(user.id), "token_type": "bearer"}

@router.get("/me", response_model=UsuarioSaida)
def me(user: Usuario = Depends(get_current_user)):
    return user
