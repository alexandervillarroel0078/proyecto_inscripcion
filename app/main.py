from fastapi import FastAPI
from app.routers import carrera, plan_estudio,nivel, materia, prerequisito  

app = FastAPI()

app.include_router(carrera.router, prefix="/carreras", tags=["Carreras"])
app.include_router(plan_estudio.router, prefix="/planes", tags=["Planes de Estudio"])
app.include_router(nivel.router, prefix="/niveles", tags=["Niveles"])
app.include_router(materia.router, prefix="/materias", tags=["Materias"])
app.include_router(prerequisito.router, prefix="/prerequisitos", tags=["Prerrequisitos"])