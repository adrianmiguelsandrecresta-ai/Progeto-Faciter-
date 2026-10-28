from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UsuarioCadastro(BaseModel):
    nome: str = Field(min_length=2, max_length=120)
    email: EmailStr
    senha: str = Field(min_length=6, max_length=128)
    tipo: str = Field(default="cliente", pattern="^(cliente|corretor)$")

class Login(BaseModel):
    email: EmailStr
    senha: str

class UsuarioSaida(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str
    email: str
    tipo: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ImovelBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=150)
    descricao: str = Field(min_length=5)
    preco: float = Field(gt=0)
    tipo: str = Field(pattern="^(casa|apartamento|terreno|comercial)$")
    cidade: str = Field(min_length=2, max_length=100)
    estado: str = Field(min_length=2, max_length=2)
    endereco: str = Field(min_length=3, max_length=180)
    quartos: int = Field(default=0, ge=0)
    banheiros: int = Field(default=0, ge=0)

class ImovelCriacao(ImovelBase):
    pass

class ImovelSaida(ImovelBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    usuario_id: int
