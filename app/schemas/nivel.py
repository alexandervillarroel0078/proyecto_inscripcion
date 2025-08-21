from pydantic import BaseModel

class NivelBase(BaseModel):
    numero: int
    nombre: str

class NivelCreate(NivelBase):
    pass

class NivelResponse(NivelBase):
    id: int

    class Config:
        orm_mode = True
