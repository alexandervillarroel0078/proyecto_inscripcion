from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.prerequisito import Prerequisito
from app.schemas.prerequisito import PrerequisitoCreate, PrerequisitoResponse

router = APIRouter()

@router.get("/", response_model=list[PrerequisitoResponse])
def listar_prerequisitos(db: Session = Depends(get_db)):
    return db.query(Prerequisito).all()

@router.post("/", response_model=PrerequisitoResponse)
def crear_prerequisito(prerequisito: PrerequisitoCreate, db: Session = Depends(get_db)):
    nuevo = Prerequisito(**prerequisito.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
