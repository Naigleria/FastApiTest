from pydantic import BaseModel


class ShowUser(BaseModel):
  username:str
  nombre:str
  apellido:str
  correo:str
  class Config():
    orm_mode=True