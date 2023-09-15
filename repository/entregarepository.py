from sqlalchemy.orm import Session

from model import entregamodel
from schema import entregaschema

def create_entrega(db: Session, Entrega: entregaschema.Entrega):
    db_user = entregamodel.Entrega(tipo=Entrega.tipo,materia=Entrega.materia,horas=Entrega.horas, nombre_actividad=Entrega.nombre_actividad,fecha=Entrega.fecha)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def list_entregas(db:Session):
    entregas= db.query(entregamodel.Entrega).all()
    return entregas

def find_by_id(db:Session, id:int):
    entrega=db.query(entregamodel.Entrega).filter(entregamodel.Entrega.id==id).first()
    return entrega

def delete_entrega(db: Session, id:int):
    entrega = db.query(entregamodel.Entrega).filter(entregamodel.Entrega.id == id).first()
    db.delete(entrega)
    db.commit()
    return entrega