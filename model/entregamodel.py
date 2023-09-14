from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval

from database import Base


class Entrega(Base):
    __tablename__ = "entregas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    materia=Column(String)
    horas = Column(Integer)
    nombre_actividad = Column(String)
    fecha= Column(Date)
