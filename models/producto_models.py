from pydantic import BaseModel

class ProductoIn(BaseModel):
    idProducto: str

class ProductoOut(BaseModel):
    productoname: str    
    precio: int
    descripcion: str