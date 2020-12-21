from db import producto_db
from db.producto_db import database_productos
from db.producto_db import ProductoInDB
from db.producto_db import get_producto, update_producto 
from db.producto_db import get_productos
from models.producto_models import ProductoIn, ProductoOut

from db import user_db
from db.user_db import database_users
from db.user_db import UserInDB
from db.user_db import get_user, update_user
from models.user_models import UserIn, UserOut

from db import categoria_db
from db.categoria_db import CategoriaInDB
from db.categoria_db import insert_categoria
from db.categoria_db import select_categorias, select_categoria
from db.categoria_db import update_categoria, delete_categoria
from models import categoria_models
from models.categoria_models import CategoriaIn, CategoriaOut


from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["http://127.0.0.1:8080","http://localhost", "http://localhost:8080", "http://127.0.0.1:8000", "http://localhost:8000", "https://tienda-virtual-app12.herokuapp.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/')
async def root():
    return {"mesagge": "Bienvenido a su Tienda Virtual"} 

@app.get('/productos/') 
async def productos():
    return get_productos()

@app.get('/productos') 
async def productos():
    return get_productos()

@app.get('/productos/{productoname}')
async def consultar_producto(productoname:str):
    if productoname in producto_db.database_productos:
        return producto_db.get_producto(productoname)   
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

@app.get('/user/auth/') 
async def usuarios():
    return {"Base de Datos": user_db.database_users}

@app.get('/user/auth') 
async def usuarios():
    return {"Base de Datos": user_db.database_users}

@app.get('/user/auth/{username}')
async def consultar_usuario(username:str):
    if username in user_db.database_users:
        return {"Base de Datos": user_db.get_user(username)}    
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe")

@app.post('/user/auth/')
async def crear_usuario(usuario:UserInDB):
    user_db.database_users[usuario.username]= usuario
    return usuario

@app.post('/user/auth')
async def crear_usuario(usuario:UserInDB):
    user_db.database_users[usuario.username]= usuario
    return usuario

@app.delete('/user/auth/')
async def borrar_usuario(user_out:UserOut):
    user_in_db = get_user(user_out.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        del user_db.database_users[user_out.username]
        return {"detail": "El usuario fue borrado"}

@app.delete('/user/auth')
async def borrar_usuario(user_out:UserOut):
    user_in_db = get_user(user_out.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    else:
        del user_db.database_users[user_out.username]
        return {"detail": "El usuario fue borrado"}

@app.put('/user/auth/')
async def actualizar_usuario(usuario:UserInDB):
    if usuario.username in database_users:
        user_db.database_users[usuario.username]= usuario
        return usuario
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe") 

@app.put('/user/auth')
async def actualizar_usuario(usuario:UserInDB):
    if usuario.productoname in database_users:
        user_db.database_users[usuario.username]= usuario
        return usuario
    else:
        raise HTTPException(status_code=404, detail="El usuario no existe")


@app.get('/info/{categoria}')
async def consultar_categoria(categoria: str):
    categoria_in_db = select_categoria(categoria)
    if categoria_in_db is None:
        raise HTTPException(status_code=404, detail="La categoria no existe")
    productos_out = []
    productos_in_db = get_productos()
    for elem in productos_in_db:
        if categoria in elem.categoria:
            productos_out.append(elem)
    return productos_out

@app.get('/info/categorias/')
async def consultar_categorias():
    categorias = select_categorias()
    return categorias

@app.post('/agregar/categoria/')
async def crear_categoria(categoria_in_db: CategoriaInDB):
    categoria = insert_categoria(categoria_in_db)
    if categoria is None:
        raise HTTPException(status_code=404, detail="La categoria ya existe")
    return categoria

@app.put('/actualizar/categoria/')
async def actualizar_categoria(categoria_in_db: CategoriaInDB):
    categoria = update_categoria(categoria_in_db)
    if categoria is None:
        raise HTTPException(status_code=404, detail="La categoria no existe")
    return categoria

@app.delete('/eliminar/{categoria}')
async def delete_categoria(categoria: str):
    categoria_in_db = delete_categoria(categoria)
    if categoria_in_db is None:
        raise HTTPException(status_code=404, detail="La categoria no existe")
    return categoria_in_db
#falta eliminar de los productos la categoria