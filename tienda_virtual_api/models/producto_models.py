from pydantic import BaseModel

class UserIn(BaseModel):
    productoname: str    

class UserOut(BaseModel):
    productoname: str    
    precio: int
    descripcion: str