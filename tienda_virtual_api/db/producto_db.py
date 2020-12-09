from typing import Dict
from pydantic import BaseModel

class ProductoInDB(BaseModel):
    productoname: str    
    precio: int
    descripcion: str
    existencia: int
    categoria: str

database_productos = Dict[str, ProductoInDB]

database_productos = {
    "rueda abdominal": ProductoInDB(**{"productoname":"rueda abdominal",
                                "precio":29900,
                                "descripcion":"La rueda es ideal para trabajo" +
                                "abdominal completo, espalda baja y fortalecimiento" +
                                " de los lumbares y generando la curvatura natural de la espalda.",
                                "existencia":7,
                                "categoria":"deportes y fitness"}),
    "patineta": ProductoInDB(**{"productoname":"patineta",
                                "precio":69900,
                                "descripcion":"Perfecta patineta diseñada para mantener horas " +
                                "y horas de diversión asegurada para los niños.",
                                "existencia":5,
                                "categoria":"juguetes"}),
}

def get_producto(productoname: str):
    if productoname in database_productos.keys():
        return database_productos[productoname]
    else:
        return None

def update_producto(producto_in_db: ProductoInDB):
    database_productos[producto_in_db.productoname] = producto_in_db
    return producto_in_db