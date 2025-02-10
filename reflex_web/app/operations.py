from pydantic import BaseModel

class User(BaseModel):
    id : int
    name: str
    surname: str
    age: int

users_fake_DB = [User(id=1, name="Angel",surname="Prado",age=35),
                 User(id=2, name="Pepe",surname="Perez",age=30),
                 User(id=3, name="Juan",surname="Hernandez",age=25)]

async def is_livehello() -> str:
    return "HOLA"

async def get_user(id: int) -> User:
    users = filter(lambda user: user.id == id, users_fake_DB)
    try:
        return list(users)[0]
    except:
        return {"code": "ACK", "description": "user not found"}