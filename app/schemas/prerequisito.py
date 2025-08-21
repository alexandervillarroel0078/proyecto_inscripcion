from pydantic import BaseModel

class PrerequisitoBase(BaseModel):
    tipo: str = "OBLIGATORIO"
    nota_min: int = 51
    materia_id: int
    prerequisito_id: int

class PrerequisitoCreate(PrerequisitoBase):
    pass

class PrerequisitoResponse(PrerequisitoBase):
    id: int

    class Config:
        from_attributes = True
