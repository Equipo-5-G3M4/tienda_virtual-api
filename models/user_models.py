from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    
class UserOut(BaseModel):
<<<<<<< HEAD
    username: str
=======
    username: str
>>>>>>> desarrollo
