from pydantic import BaseModel


class ProductoInDB(BaseModel):
    productoname: str
    precio: int
    descripcion: str
    existencia: int
    categoria: str
    imagen: str


database_productos = {
    "rueda abdominal": ProductoInDB(**{"productoname": "rueda abdominal",
                                       "precio": 29900,
                                       "descripcion": "La rueda es ideal para trabajo" +
                                                      "abdominal completo, espalda baja y fortalecimiento" +
                                                      " de los lumbares y generando la curvatura natural de la espalda.",
                                       "existencia": 7,
                                       "categoria": "deportes y fitness",
                                       "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607915160/Tienda/sports_rollerabswheel.jpg"}),
    "patineta": ProductoInDB(**{"productoname": "patineta",
                                "precio": 69900,
                                "descripcion": "Perfecta patineta diseñada para mantener horas " +
                                               "y horas de diversión asegurada para los niños.",
                                "existencia": 5,
                                "categoria": "deportes y fitness",
                                "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911018/Tienda/sports_skate03.jpg"}),
    "reloj": ProductoInDB(**{"productoname": "reloj",
                             "precio": 169900,
                             "descripcion": "Cómodo reloj resistente al agua " +
                                            "con un fino toque plateado.",
                             "existencia": 10,
                             "categoria": "relojes",
                             "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911011/Tienda/watches_05.jpg"}),
    "iphone": ProductoInDB(**{"productoname": "iphone",
                              "precio": 1800000,
                              "descripcion": "Revolucionario teléfono marca Apple " +
                                             "ideal para el ejecutivo de hoy.",
                              "existencia": 15,
                              "categoria": "tecnología",
                              "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911025/Tienda/technology_phone_iphone_white.jpg"}),
    "maceta": ProductoInDB(**{"productoname": "maceta",
                              "precio": 24900,
                              "descripcion": "Delicada maceta para que sus plantas " +
                                             "se sientan como en el bosque.",
                              "existencia": 8,
                              "categoria": "hogar",
                              "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902872/Tienda/plants_pot05.jpg"}),
    "gafas": ProductoInDB(**{"productoname": "gafas",
                             "precio": 99900,
                             "descripcion": "Elegante diseño y con un filtro solar " +
                                            "de la más alta categoría.",
                             "existencia": 10,
                             "categoria": "gafas",
                             "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902863/Tienda/glasses_black02.jpg"}),
    "maquillaje": ProductoInDB(**{"productoname": "maquillaje",
                                  "precio": 55900,
                                  "descripcion": "Base de maquillaje con tonos calidos, " +
                                                 "perfecto para la mujer actual.",
                                  "existencia": 22,
                                  "categoria": "mujeres",
                                  "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911020/Tienda/makeup03.jpg"}),
    "bicicleta": ProductoInDB(**{"productoname": "bicicleta",
                                 "precio": 890000,
                                 "descripcion": "Bicicleta de 21 cambios todoterreno, " +
                                                "para ser usada en cualquier situación.",
                                 "existencia": 13,
                                 "categoria": "deportes y fitness",
                                 "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911013/Tienda/sports_bycicle.jpg"}),
    "silla": ProductoInDB(**{"productoname": "silla",
                             "precio": 222900,
                             "descripcion": "Silla con un toque clásico, " +
                                            "tanto para jardines como interiores.",
                             "existencia": 4,
                             "categoria": "hogar",
                             "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607902871/Tienda/furniture_chair.jpg"}),
    "tenis": ProductoInDB(**{"productoname": "tenis",
                             "precio": 240900,
                             "descripcion": "Tenis nike con bota, con un llamativo " +
                                            "tono verde neon.",
                             "existencia": 6,
                             "categoria": "hombres",
                             "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911010/Tienda/clothing_men_shoes11.jpg"}),
    "lampara": ProductoInDB(**{"productoname": "lampara",
                               "precio": 125900,
                               "descripcion": "Lámpara con un fino toque contemporaneo, " +
                                              "con una gran bombilla para esas noches obscuras.",
                               "existencia": 13,
                               "categoria": "hogar",
                               "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911017/Tienda/furniture_lamp.jpg"}),
    "reloj de pared": ProductoInDB(**{"productoname": "reloj de pared",
                                      "precio": 35900,
                                      "descripcion": "Sobrio reloj de pared de color blanco y " +
                                                     "con manecillas negras.",
                                      "existencia": 4,
                                      "categoria": "hogar",
                                      "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911010/Tienda/furniture_watch.jpg"}),
    "mug": ProductoInDB(**{"productoname": "mug",
                           "precio": 27900,
                           "descripcion": "Un mug fino con un hermoso color blanco mate " +
                                          "y tecnólgía que evita la perdida de calor.",
                           "existencia": 33,
                           "categoria": "hogar",
                           "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911019/Tienda/tableware_mug02.jpg"}),
    "microscopio": ProductoInDB(**{"productoname": "microscopio",
                                   "precio": 222900,
                                   "descripcion": "Microscopio potente con 64x de aumento, " +
                                                  "para aprender y sorprenderse con lo que no se ve a simple vista.",
                                   "existencia": 4,
                                   "categoria": "tecnología",
                                   "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911015/Tienda/technology_microscope.jpg"}),
    "bandeja con rejilla": ProductoInDB(**{"productoname": "bandeja con rejilla",
                                           "precio": 240900,
                                           "descripcion": "Bandeja adecuada para hornos en material " +
                                                          "duradero y con garantía de fábrica.",
                                           "existencia": 15,
                                           "categoria": "hogar",
                                           "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911020/Tienda/various_gridtray.jpg"}),
    "camara": ProductoInDB(**{"productoname": "camara",
                              "precio": 125900,
                              "descripcion": "Una hermosa cámara Fujifilm, " +
                                             "de 64Mp y con un lente de 35mm.",
                              "existencia": 5,
                              "categoria": "tecnología",
                              "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911021/Tienda/technology_camera_fujifilm.jpg"}),
    "reloj inteligente": ProductoInDB(**{"productoname": "reloj inteligente",
                                         "precio": 155900,
                                         "descripcion": "Smartwatch con potente procesador " +
                                                        "contador de pasos, medidor de pulso y notificación de mensajes de redes.",
                                         "existencia": 4,
                                         "categoria": "tecnología",
                                         "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911021/Tienda/technology_smartwatch01.jpg"}),
    "jarron": ProductoInDB(**{"productoname": "jarron",
                              "precio": 22900,
                              "descripcion": "Bello jarrón para tus plantas " +
                                             "artificiales o naturales.",
                              "existencia": 11,
                              "categoria": "hogar",
                              "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911023/Tienda/plants_vase01.jpg"}),
    "perfume": ProductoInDB(**{"productoname": "perfume",
                               "precio": 101900,
                               "descripcion": "Fino perfume Coco Chanel, con " +
                                              "aromas y fragancias frorales y con un leve toque frutal.",
                               "existencia": 16,
                               "categoria": "mujeres",
                               "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911011/Tienda/perfume03.jpg"}),
    "macbook": ProductoInDB(**{"productoname": "macbook",
                               "precio": 3222900,
                               "descripcion": "Poderoso 'portátil' de la marca " +
                                              "Apple con 4Tb de DD y 16 gigas de memoria RAM.",
                               "existencia": 14,
                               "categoria": "tecnología",
                               "imagen": "https://res.cloudinary.com/kiriloff/image/upload/v1607911009/Tienda/technology_macbook.jpg"}),

}


def get_producto(productoname: str):
    if productoname in database_productos.keys():
        return database_productos[productoname]
    else:
        return None


def update_producto(producto_in_db: ProductoInDB):
    database_productos[producto_in_db.productoname] = producto_in_db
    return producto_in_db


def get_productos():
    productos = []
    for e in database_productos:
        productos.append(database_productos[e])
    return productos
