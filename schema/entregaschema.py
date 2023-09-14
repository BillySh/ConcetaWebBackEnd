from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class Entrega(BaseModel):
    tipo : str
    materia: str
    horas : int
    nombre_actividad :str
    fecha: date