from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

#import app models
from app.models.user import User
from app.models.updateUser import UpdateUser
from app.models.showUser import ShowUser

router = APIRouter(
  prefix="/user",
  tags=["Users"]
)

@router.get('/', response_model=List[ShowUser])
async def GetAllUsers(db: Session = Depends(get_db)):
  data=  db.query(models.User).all() #aqui no es necesario "await" ya que una lista no es un objeto "Awaitable"
  print(data)
  return data

@router.post('/')
async def CreateUser(user:User,db: Session = Depends(get_db)):
  usuario=user.dict()
  nuevo_usuario= models.User(
    username=usuario["username"],
    password=usuario["password"],
    nombre=usuario["nombre"],
    apellido=usuario["apellido"],
    direccion=usuario["direccion"],
    telefono=usuario["telefono"],
    correo=usuario["correo"],
  )
  db.add(nuevo_usuario)
  await db.commit()
  db.refresh(nuevo_usuario)
  return {"message": "Usuario creado exitosamente!"}

@router.get('/{user_id}', response_model=ShowUser)
async def GetUserById(user_id:int,db: Session = Depends(get_db)):
  usuario= await db.query(models.User).filter(models.User.id==user_id).first()
  if not usuario:
    return {"message":"Usuario no encontrado !!"}
  return usuario

@router.delete('/{user_id}')
async def DeleteUserById(user_id:int, db: Session = Depends(get_db)):
  usuario= db.query(models.User).filter(models.User.id==user_id)
  if not usuario.first():
    return {"message":"Usuario no encontrado !!"}
  usuario.delete(synchronize_session=False)
  await db.commit()
  return {"message":"Usuario eliminado exitosamente"}

@router.patch('/{user_id}')
async def UpdateUserById(user_id:int, updateUser:UpdateUser,db: Session = Depends(get_db)):
  usuario=  db.query(models.User).filter(models.User.id==user_id)
  if not usuario.first():
    return {"message":"Usuario no encontrado !!"}
  #la sig linea nos permite actualizar solo los campos
  #del usuario que llegan desde el json body
  usuario.update(updateUser.dict(exclude_unset=True))
  await db.commit()
  return {"message":"Usuario actualizado exitosamente!"}

