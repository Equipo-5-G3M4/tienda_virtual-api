from typing import (Dict, List)
from pydantic import BaseModel


class ProductoInDB(BaseModel):
    idProducto: str
    productoname: str
    precio: int
    descripcion: str
    existencia: int
    categoria: List[str]
    imagen: str


database_productos = {
    "02297a70-2839-45dc-aead-8fed7241580a": ProductoInDB(**{
                                "idProducto": "02297a70-2839-45dc-aead-8fed7241580a",
                                "productoname":"rueda abdominal",
                                "precio":29900,
                                "descripcion":"La rueda es ideal para trabajo" +
                                "abdominal completo, espalda baja y fortalecimiento" +
                                " de los lumbares y generando la curvatura natural de la espalda.",
                                "existencia":7,
                                "categoria":["deportes","fitness"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607915160/Tienda/sports_rollerabswheel.jpg"
                                }),
    "d8fee2ac-14fc-421c-97da-5606ded76b1a": ProductoInDB(**{
                                "idProducto": "d8fee2ac-14fc-421c-97da-5606ded76b1a",
                                "productoname":"patineta",
                                "precio":69900,
                                "descripcion":"Perfecta patineta diseñada para mantener horas " +
                                "y horas de diversión asegurada para los niños.",
                                "existencia":5,
                                "categoria":["deportes","fitness"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911018/Tienda/sports_skate03.jpg"}),
    "371a86ba-3e1c-43ee-8267-7a23500e2d3b": ProductoInDB(**{
                                "idProducto": "371a86ba-3e1c-43ee-8267-7a23500e2d3b",
                                "productoname":"reloj",
                                "precio":169900,
                                "descripcion":"Cómodo reloj resistente al agua " +
                                "con un fino toque plateado.",
                                "existencia":10,
                                "categoria":["relojes"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911011/Tienda/watches_05.jpg"}),
    "850cc12a-72d3-47e8-a6b3-4aa629cc9660": ProductoInDB(**{
                                "idProducto": "850cc12a-72d3-47e8-a6b3-4aa629cc9660",
                                "productoname":"iphone",
                                "precio":1800000,
                                "descripcion":"Revolucionario teléfono marca Apple " +
                                "ideal para el ejecutivo de hoy.",
                                "existencia":15,
                                "categoria":["tecnología"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911025/Tienda/technology_phone_iphone_white.jpg" }),
    "390df4a0-1b0b-4611-843f-e32dc9e777ce": ProductoInDB(**{
                                "idProducto": "390df4a0-1b0b-4611-843f-e32dc9e777ce",
                                "productoname":"maceta",
                                "precio":24900,
                                "descripcion":"Delicada maceta para que sus plantas " +
                                "se sientan como en el bosque.",
                                "existencia":8,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902872/Tienda/plants_pot05.jpg"}),
    "5b0f607a-3ec9-42f4-a67d-eed5ad0a5501": ProductoInDB(**{
                                "idProducto": "5b0f607a-3ec9-42f4-a67d-eed5ad0a5501",
                                "productoname":"gafas",
                                "precio":99900,
                                "descripcion":"Elegante diseño y con un filtro solar " +
                                "de la más alta categoría.",
                                "existencia":10,
                                "categoria":["gafas"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902863/Tienda/glasses_black02.jpg"}),
    "e26c2218-6746-4729-8ac9-539126f0bcdc": ProductoInDB(**{
                                "idProducto": "e26c2218-6746-4729-8ac9-539126f0bcdc",
                                "productoname":"maquillaje",
                                "precio":55900,
                                "descripcion":"Base de maquillaje con tonos calidos, " +
                                "perfecto para la mujer actual.",
                                "existencia":22,
                                "categoria":["mujeres"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911020/Tienda/makeup03.jpg"}),
    "320d77f7-858c-4204-9e23-eee82bc072e9": ProductoInDB(**{
                                "idProducto": "320d77f7-858c-4204-9e23-eee82bc072e9",
                                "productoname":"bicicleta",
                                "precio":890000,
                                "descripcion":"Bicicleta de 21 cambios todoterreno, " +
                                "para ser usada en cualquier situación.",
                                "existencia":13,
                                "categoria":["deportes","fitness"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911013/Tienda/sports_bycicle.jpg"}),
    "b782cf04-8db6-4a1f-b0ba-50f5178319ea": ProductoInDB(**{
                                "idProducto": "b782cf04-8db6-4a1f-b0ba-50f5178319ea",
                                "productoname":"silla",
                                "precio":222900,
                                "descripcion":"Silla con un toque clásico, " +
                                "tanto para jardines como interiores.",
                                "existencia":4,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902871/Tienda/furniture_chair.jpg"}),
    "be803e24-91a9-4fdd-a717-85f1e9824e8e": ProductoInDB(**{
                                "idProducto": "be803e24-91a9-4fdd-a717-85f1e9824e8e",
                                "productoname":"tenis",
                                "precio":240900,
                                "descripcion":"Tenis nike con bota, con un llamativo " +
                                "tono verde neon.",
                                "existencia":6,
                                "categoria":["hombres"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911010/Tienda/clothing_men_shoes11.jpg" }),
    "e32f240d-35c8-40d4-a51f-a5450ace5d73": ProductoInDB(**{
                                "idProducto": "e32f240d-35c8-40d4-a51f-a5450ace5d73",
                                "productoname":"lampara",
                                "precio":125900,
                                "descripcion":"Lámpara con un fino toque contemporaneo, " +
                                "con una gran bombilla para esas noches obscuras.",
                                "existencia":13,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911017/Tienda/furniture_lamp.jpg"}),
    "c1f94e84-acc5-443d-b193-9bfa5c58e352": ProductoInDB(**{
                                "idProducto": "c1f94e84-acc5-443d-b193-9bfa5c58e352",
                                "productoname":"reloj de pared",
                                "precio":35900,
                                "descripcion":"Sobrio reloj de pared de color blanco y " +
                                "con manecillas negras.",
                                "existencia":4,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911010/Tienda/furniture_watch.jpg"}),
    "1c910550-9d75-47ad-92e4-5f09c095c1ec": ProductoInDB(**{
                                "idProducto": "1c910550-9d75-47ad-92e4-5f09c095c1ec",
                                "productoname":"mug",
                                "precio":27900,
                                "descripcion":"Un mug fino con un hermoso color blanco mate " +
                                "y tecnólgía que evita la perdida de calor.",
                                "existencia":33,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911019/Tienda/tableware_mug02.jpg"}),
    "d0c55dd7-ccd2-4613-8819-e643a096233e": ProductoInDB(**{
                                "idProducto": "d0c55dd7-ccd2-4613-8819-e643a096233e",
                                "productoname":"microscopio",
                                "precio":222900,
                                "descripcion":"Microscopio potente con 64x de aumento, " +
                                "para aprender y sorprenderse con lo que no se ve a simple vista.",
                                "existencia":4,
                                "categoria":["tecnología"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911015/Tienda/technology_microscope.jpg"}),
    "55f3947b-45c4-4807-be65-34e8997d8629": ProductoInDB(**{
                                "idProducto": "55f3947b-45c4-4807-be65-34e8997d8629",
                                "productoname":"bandeja con rejilla",
                                "precio":240900,
                                "descripcion":"Bandeja adecuada para hornos en material " +
                                "duradero y con garantía de fábrica.",
                                "existencia":15,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911020/Tienda/various_gridtray.jpg" }),
    "9088fb98-ae36-47a9-8dd3-0b4c19e8c41a": ProductoInDB(**{
                                "idProducto": "9088fb98-ae36-47a9-8dd3-0b4c19e8c41a",
                                "productoname":"camara",
                                "precio":125900,
                                "descripcion":"Una hermosa cámara Fujifilm, " +
                                "de 64Mp y con un lente de 35mm.",
                                "existencia":5,
                                "categoria":["tecnología"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911021/Tienda/technology_camera_fujifilm.jpg"}),
    "c882fbe5-d7d6-47cf-a9b0-62942a9efc82": ProductoInDB(**{
                                "idProducto": "c882fbe5-d7d6-47cf-a9b0-62942a9efc82",
                                "productoname":"reloj inteligente",
                                "precio":155900,
                                "descripcion":"Smartwatch con potente procesador " +
                                "contador de pasos, medidor de pulso y notificación de mensajes de redes.",
                                "existencia":4,
                                "categoria":["tecnología"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911021/Tienda/technology_smartwatch01.jpg"}),
    "163f9425-bfa6-4bc5-aa7a-1fdb2ca1c26f": ProductoInDB(**{
                                "idProducto": "163f9425-bfa6-4bc5-aa7a-1fdb2ca1c26f",
                                "productoname":"jarron",
                                "precio":22900,
                                "descripcion":"Bello jarrón para tus plantas " +
                                "artificiales o naturales.",
                                "existencia":11,
                                "categoria":["hogar"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911023/Tienda/plants_vase01.jpg"}),
    "9c7ffea2-81e1-488a-8de4-a5443c4baedc": ProductoInDB(**{
                                "idProducto": "9c7ffea2-81e1-488a-8de4-a5443c4baedc",
                                "productoname":"perfume",
                                "precio":101900,
                                "descripcion":"Fino perfume Coco Chanel, con " +
                                "aromas y fragancias frorales y con un leve toque frutal.",
                                "existencia":16,
                                "categoria":["mujeres"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911011/Tienda/perfume03.jpg"}),
    "7c7ee33f-b38e-4b77-a601-432dc1ec2adc": ProductoInDB(**{
                                "idProducto": "7c7ee33f-b38e-4b77-a601-432dc1ec2adc",
                                "productoname":"macbook",
                                "precio":3222900,
                                "descripcion":"Poderoso 'portátil' de la marca " +
                                "Apple con 4Tb de DD y 16 gigas de memoria RAM.",
                                "existencia":14,
                                "categoria":["tecnología"],
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911009/Tienda/technology_macbook.jpg"}),
    
}

def get_producto_by_id(idProducto: str):
    if idProducto in database_productos.keys():
        return database_productos[idProducto]
    else:
        return None

def get_producto_by_name(productoName: str):
    productos = list(database_productos.values())
    for producto in productos:
        if producto.productoname == productoName:
            return producto
    return None

def update_producto(producto_in_db: ProductoInDB):
    database_productos[producto_in_db.productoname] = producto_in_db
    return producto_in_db


def get_productos():
    productos = []
    for e in database_productos:
        productos.append(database_productos[e])
    return productos
