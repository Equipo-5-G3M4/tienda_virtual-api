from pydantic import BaseModel


class CategoriaIn(BaseModel):
    nombre: str
    imagen: str


class CategoriaOut(BaseModel):
    id: int
    nombre: str
    imagen: str
