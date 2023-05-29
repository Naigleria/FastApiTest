from pydantic import BaseModel
from typing import Optional

class UpdateUser(BaseModel): #Schema
  username:str =None
  password:str =None
  nombre:str =None
  apellido:str =None
  direccion:str=None
  telefono:str=None
  correo:str=None