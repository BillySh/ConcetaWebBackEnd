from fastapi import FastAPI,Depends
from schema.entregaschema import Entrega
from repository import entregarepository
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, HTTPException, Body
from pydantic import BaseModel

app=FastAPI()
class Data(BaseModel):
    id: int

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##Pagina del frente. ------------------------------------------
@app.get("/")
async def list_entregas(db: Session = Depends(get_db)):
    entregas=entregarepository.list_entregas(db)
    return entregas

##Creación de tarea. -------------------------------------
@app.post("/entrega/create",response_model=Entrega)
async def create_entregas(entrega:Entrega, db: Session = Depends(get_db)):
    entrega=entregarepository.create_entrega(db,entrega)
    return entrega
##Eliminar una entrega

@app.get("/entrega/find/{id}",response_model=Entrega)
async def find_by_id(db:Session=Depends(get_db),id:int=0):
    print(id)
    user=entregarepository.find_by_id(db,id)
    print(user)
    return user



@app.post("/entrega/delete", response_model=Entrega)
async def delete_entrega(id : int = Body(..., embed=True), db: Session = Depends(get_db)):
    success = entregarepository.delete_entrega(db, id)
    if success:
        return {"message": "Entrega deleted successfully"}
    else: 
        print(id)

##-------------------------------------------------------------

"""
@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message":f"Hello {name}"}


@app.post("/hello-post")
async def hello_name(user:User):
    return {"message":f"Hello {user.name}"}

@app.post("/user/create",response_model=User)
async def create_user(user:User, db: Session = Depends(get_db)):
    user=userrepository.create_user(db,user)
    return user

@app.get("/user/list",response_model=list[User])
async def list_users(db: Session = Depends(get_db)):
    users=userrepository.list_users(db)
    return users

@app.get("/user/find/{id}",response_model=User)
async def find_by_id(db:Session=Depends(get_db),id:int=0):
    print(id)
    user=userrepository.find_by_id(db,id)
    print(user)
    return user
"""