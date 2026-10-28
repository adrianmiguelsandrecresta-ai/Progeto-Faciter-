from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Imovel, Usuario
from ..schemas import ImovelCriacao, ImovelSaida
from ..dependencies import get_current_user

router = APIRouter(prefix="/imoveis", tags=["Imóveis"])

@router.get("", response_model=list[ImovelSaida])
def listar(cidade: str | None = Query(None), tipo: str | None = Query(None), db: Session = Depends(get_db)):
    query = db.query(Imovel)
    if cidade: query = query.filter(Imovel.cidade.ilike(f"%{cidade}%"))
    if tipo: query = query.filter(Imovel.tipo == tipo)
    return query.order_by(Imovel.id.desc()).all()

@router.get("/{imovel_id}", response_model=ImovelSaida)
def buscar(imovel_id: int, db: Session = Depends(get_db)):
    imovel = db.get(Imovel, imovel_id)
    if not imovel: raise HTTPException(404, "Imóvel não encontrado")
    return imovel

@router.post("", response_model=ImovelSaida, status_code=201)
def criar(data: ImovelCriacao, db: Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    imovel = Imovel(**data.model_dump(), usuario_id=user.id)
    db.add(imovel); db.commit(); db.refresh(imovel)
    return imovel

@router.put("/{imovel_id}", response_model=ImovelSaida)
def atualizar(imovel_id: int, data: ImovelCriacao, db: Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    imovel = db.get(Imovel, imovel_id)
    if not imovel: raise HTTPException(404, "Imóvel não encontrado")
    if imovel.usuario_id != user.id: raise HTTPException(403, "Você não pode alterar este imóvel")
    for key, value in data.model_dump().items(): setattr(imovel, key, value)
    db.commit(); db.refresh(imovel)
    return imovel

@router.delete("/{imovel_id}", status_code=204)
def excluir(imovel_id: int, db: Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    imovel = db.get(Imovel, imovel_id)
    if not imovel: raise HTTPException(404, "Imóvel não encontrado")
    if imovel.usuario_id != user.id: raise HTTPException(403, "Você não pode excluir este imóvel")
    db.delete(imovel); db.commit()
