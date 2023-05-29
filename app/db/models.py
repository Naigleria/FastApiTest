from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship


##Tabla/Modelo
#Los campos que tienen 'unique' truena cuando se quiere repetir
#el username o el correo
class User(Base):
  __tablename__="user"
  id = Column(Integer, primary_key=True, autoincrement=True)
  username=Column(String, unique=True)
  password=Column(String)
  nombre=Column(String)
  apellido=Column(String)
  direccion=Column(String)
  telefono=Column(String)
  correo=Column(String, unique=True)
  creacion=Column(DateTime, default=datetime.now, onupdate=datetime.now)
  estado=Column(Boolean, default=False)
  venta = relationship("Venta", backref="user", cascade="delete,merge")

class Venta(Base):
  __tablename__="venta"
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id=Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
  venta =Column(Integer)
  ventas_productos=Column(Integer)