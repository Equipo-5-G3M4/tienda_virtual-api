from pydantic import BaseModel


class CategoriaInDB(BaseModel):
    id: int = 0
    nombre: str
    imagen: str


database_categorias = {
    0: CategoriaInDB(**{'id': 0, 'nombre': 'deportes', 'imagen': "url"}),
    1: CategoriaInDB(**{'id': 1, 'nombre': 'fitness', 'imagen': "url"}),
    2: CategoriaInDB(**{'id': 2, 'nombre': 'relojes', 'imagen': "url"}),
    3: CategoriaInDB(**{'id': 3, 'nombre': 'tecnología', 'imagen': "url"}),
    4: CategoriaInDB(**{'id': 4, 'nombre': 'hogar', 'imagen': "url"}),
    5: CategoriaInDB(**{'id': 5, 'nombre': 'gafas', 'imagen': "url"}),
    6: CategoriaInDB(**{'id': 6, 'nombre': 'mujeres', 'imagen': "url"}),
    7: CategoriaInDB(**{'id': 7, 'nombre': 'hombres', 'imagen': "url"})
}
generador = {'id': 9}


def insert_categoria(categoria_in_db: CategoriaInDB):
    for elem in database_categorias:
        if database_categorias[elem].nombre == categoria_in_db.nombre:
            return None
    categoria_in_db.id = generador['id']
    database_categorias[generador['id']] = categoria_in_db
    generador['id'] += 1
    return categoria_in_db


def delete_categoria(nombre_categoria: str):
    for elem in database_categorias:
        if database_categorias[elem].nombre == nombre_categoria:
            categoria_in_db = database_categorias.pop(elem)
            return categoria_in_db
    return None


def update_categoria(categoria_in_db: CategoriaInDB):
    if categoria_in_db.id in database_categorias.keys():
        for elem in database_categorias:
            if elem != categoria_in_db.id and database_categorias[elem].nombre == categoria_in_db.nombre:
                return None
        database_categorias[categoria_in_db.id] = categoria_in_db
        return categoria_in_db
    return None


def select_categoria(nombre_categoria: str):
    for elem in database_categorias:
        if database_categorias[elem].nombre == nombre_categoria:
            return elem
    return None


def select_categorias():
    categorias = []
    for elem in database_categorias:
        categorias.append(database_categorias[elem])
    return categorias
