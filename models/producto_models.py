from pydantic import BaseModel


class ProductoIn(BaseModel):
    productoname: str    


class ProductoOut(BaseModel):
    productoname: str    
    precio: int
    descripcion: str
    imagen: str
