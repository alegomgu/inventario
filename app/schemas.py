from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombre: str

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True
