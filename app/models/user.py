from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model
class User(BaseModel): #Schema
  username:str
  password:str
  nombre:str
  apellido:str
  direccion:Optional[str]
  telefono:str
  correo:str
  creacion_user:datetime = datetime.now()