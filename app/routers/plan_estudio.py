from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.plan_estudio import PlanEstudio
from app.models.carrera import Carrera
from app.schemas.plan_estudio import PlanEstudioResponse, PlanEstudioCreate

router = APIRouter()

@router.get("/", response_model=list[PlanEstudioResponse])
def listar_planes(db: Session = Depends(get_db)):
    return db.query(PlanEstudio).all()

@router.post("/", response_model=PlanEstudioResponse)
def crear_plan(plan: PlanEstudioCreate, db: Session = Depends(get_db)):
    # Validar que exista la carrera
    carrera = db.query(Carrera).filter(Carrera.id == plan.carrera_id).first()
    if not carrera:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")

    nuevo_plan = PlanEstudio(
        nombre=plan.nombre,
        año=plan.año,
        vigente_desde=plan.vigente_desde,
        estado=plan.estado,
        carrera_id=plan.carrera_id
    )
    db.add(nuevo_plan)
    db.commit()
    db.refresh(nuevo_plan)
    return nuevo_plan
