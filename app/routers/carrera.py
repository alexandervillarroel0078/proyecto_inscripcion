#app/routers/carrera.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.carrera import Carrera
from app.schemas.carrera import CarreraResponse, CarreraCreate

router = APIRouter()

@router.get("/", response_model=list[CarreraResponse])
def listar_carreras(db: Session = Depends(get_db)):
    return db.query(Carrera).all()

@router.post("/", response_model=CarreraResponse)
def create_carrera(carrera: CarreraCreate, db: Session = Depends(get_db)):
    # Verificar que no exista ya
    db_carrera = db.query(Carrera).filter(Carrera.nombre == carrera.nombre).first()
    if db_carrera:
        raise HTTPException(status_code=400, detail="La carrera ya existe")

    nueva_carrera = Carrera(nombre=carrera.nombre)
    db.add(nueva_carrera)
    db.commit()
    db.refresh(nueva_carrera)
    return nueva_carrera
