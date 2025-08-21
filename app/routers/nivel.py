from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.nivel import Nivel
from app.schemas.nivel import NivelResponse, NivelCreate

router = APIRouter()

@router.get("/", response_model=list[NivelResponse])
def listar_niveles(db: Session = Depends(get_db)):
    return db.query(Nivel).all()

@router.post("/", response_model=NivelResponse)
def crear_nivel(nivel: NivelCreate, db: Session = Depends(get_db)):
    db_nivel = db.query(Nivel).filter(Nivel.numero == nivel.numero).first()
    if db_nivel:
        raise HTTPException(status_code=400, detail="Ese nivel ya existe")

    nuevo = Nivel(numero=nivel.numero, nombre=nivel.nombre)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
