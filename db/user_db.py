from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str

# Diccionario
database_users = Dict[str, UserInDB]

database_users = {
    "admin": UserInDB(**{"username":"admin",
                            "password":"admin"}),

    "leonardo": UserInDB(**{"username":"leonardo",
                            "password":"1234"}),

    "roberto": UserInDB(**{"username":"roberto",
                            "password":"4321"}),

    "daniel": UserInDB(**{"username":"daniel",
                            "password":"5678"}),

    "felipe": UserInDB(**{"username":"felipe",
                            "password":"8765"}),

    "diego": UserInDB(**{"username":"diego",
                            "password":"0987"}),
}

def get_user(username: str):    
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db