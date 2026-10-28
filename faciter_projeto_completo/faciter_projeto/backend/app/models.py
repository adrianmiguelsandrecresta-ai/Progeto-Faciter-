from datetime import datetime, timezone
from sqlalchemy import String, Float, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(160), unique=True, index=True, nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    tipo: Mapped[str] = mapped_column(String(20), default="cliente", nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    imoveis: Mapped[list["Imovel"]] = relationship(back_populates="proprietario", cascade="all, delete-orphan")

class Imovel(Base):
    __tablename__ = "imoveis"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    tipo: Mapped[str] = mapped_column(String(30), nullable=False)
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)
    endereco: Mapped[str] = mapped_column(String(180), nullable=False)
    quartos: Mapped[int] = mapped_column(Integer, default=0)
    banheiros: Mapped[int] = mapped_column(Integer, default=0)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    proprietario: Mapped[Usuario] = relationship(back_populates="imoveis")

class Favorito(Base):
    __tablename__ = "favoritos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    imovel_id: Mapped[int] = mapped_column(ForeignKey("imoveis.id", ondelete="CASCADE"), nullable=False)
