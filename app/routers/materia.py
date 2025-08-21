from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.materia import Materia
from app.schemas.materia import MateriaCreate, MateriaResponse

router = APIRouter()

@router.get("/", response_model=list[MateriaResponse])
def listar_materias(db: Session = Depends(get_db)):
    return db.query(Materia).all()

@router.post("/", response_model=MateriaResponse)
def crear_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    db_materia = db.query(Materia).filter(Materia.codigo == materia.codigo).first()
    if db_materia:
        raise HTTPException(status_code=400, detail="La materia ya existe")

    nueva = Materia(**materia.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
