from pydantic import BaseModel

class CarreraBase(BaseModel):
    nombre: str

class CarreraCreate(CarreraBase):
    pass

class CarreraResponse(CarreraBase):
    id: int

    class Config:
        from_attributes = True   # antes era orm_mode = True
