from pydantic import BaseModel

class MateriaBase(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    horas_sem: int

class MateriaCreate(MateriaBase):
    nivel_id: int
    plan_id: int

class MateriaResponse(MateriaBase):
    id: int
    nivel_id: int
    plan_id: int

    class Config:
        from_attributes = True
