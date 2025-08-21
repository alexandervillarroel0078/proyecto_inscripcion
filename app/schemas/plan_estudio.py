from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.schemas.carrera import CarreraResponse

class PlanEstudioBase(BaseModel):
    nombre: str
    año: str
    vigente_desde: Optional[date] = None
    estado: Optional[bool] = True

class PlanEstudioCreate(PlanEstudioBase):
    carrera_id: int

class PlanEstudioResponse(PlanEstudioBase):
    id: int
    carrera: CarreraResponse   # incluir datos de la carrera
    class Config:
        from_attributes = True
