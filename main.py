from db import producto_db
from db.producto_db import database_productos
from db.producto_db import ProductoInDB
from db.producto_db import get_producto, update_producto 
from models.producto_models import ProductoIn, ProductoOut
from db import user_db
from db.user_db import database_users
from db.user_db import UserInDB
from db.user_db import get_user, update_user
from models.user_models import UserIn, UserOut
from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()

@app.get('/')
async def root():
    return {"mesagge": "Bienvenido a su Tienda Virtual"} 

@app.get('/productos/') 
async def productos():
    return {"Base de Datos": producto_db.database_productos}

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

@app.post('/productos')
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

@app.delete('/productos')
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

@app.put('/productos')
async def actualizar_producto(producto:ProductoInDB):
    if producto.productoname in database_productos:
        producto_db.database_productos[producto.productoname]= producto
        return producto
    else:
        raise HTTPException(status_code=404, detail="El producto no existe")

@app.get('/usuarios/') 
async def usuarios():
    return {"Base de Datos": user_db.database_users}

@app.get('/usuarios') 
async def usuarios():
    return {"Base de Datos": user_db.database_users}

@app.get('/usuarios/{username}')
async def consultar_usuario(username:str):
    if username in user_db.database_users:
        return {"Base de Datos": user_db.get_user(username)}    
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe")

@app.post('/usuarios/')
async def crear_usuario(usuario:UserInDB):
    user_db.database_users[usuario.username]= usuario
    return usuario

@app.post('/usuarios')
async def crear_usuario(usuario:UserInDB):
    user_db.database_users[usuario.username]= usuario
    return usuario

@app.delete('/usuarios/')
async def borrar_usuario(user_out:UserOut):
    user_in_db = get_user(user_out.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        del user_db.database_users[user_out.username]
        return {"detail": "El usuario fue borrado"}

@app.delete('/usuarios')
async def borrar_usuario(user_out:UserOut):
    user_in_db = get_user(user_out.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        del user_db.database_users[user_out.username]
        return {"detail": "El usuario fue borrado"}

@app.put('/usuarios/')
async def actualizar_usuario(usuario:UserInDB):
    if usuario.username in database_users:
        user_db.database_users[usuario.username]= usuario
        return usuario
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe") 

@app.put('/usuarios')
async def actualizar_usuario(usuario:UserInDB):
    if usuario.productoname in database_users:
        user_db.database_users[usuario.username]= usuario
        return usuario
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe")

