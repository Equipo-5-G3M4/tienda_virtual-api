from db import producto_db
from db.producto_db import database_productos
from db.producto_db import ProductoInDB
from db.producto_db import get_producto, update_producto 
from models.producto_models import ProductoIn, ProductoOut
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get('/')
async def root():
    return {"mesagge": "Bienvenido a su Tienda Virtual"} 

@app.get('/productos') 
async def productos():
    return {"Base de Datos": producto_db.database_productos} 

@app.get('/productos/{productoname}')
async def consultar_producto(productoname:str):
    if productoname in producto_db.database_productos:
        return {"Base de Datos": producto_db.get_producto(productoname)}    
    else:
        raise HTTPException(status_code=404, detail="El producto no existe")

@app.post('/productos/')
async def crear_producto(producto:ProductoInDB):
    producto_db.database_productos[producto.productoname]= producto
    return producto

@app.delete('/productos/')
async def borrar_producto(producto_out:ProductoOut):
    producto_in_db = get_producto(producto_out.productoname)
    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no existe")
    else:
        del producto_db.database_productos[producto_out.productoname]
        return {"detail": "El producto fue borrado"}

@app.put('/productos/')
async def actualizar_producto(producto:ProductoInDB):
    if producto.productoname in database_productos:
        producto_db.database_productos[producto.productoname]= producto
        return producto
    else:
        raise HTTPException(status_code=404, detail="El producto no existe")   