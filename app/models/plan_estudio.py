from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PlanEstudio(Base):
    __tablename__ = "plan_estudio"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    año = Column(String(20), nullable=False)
    vigente_desde = Column(Date, nullable=True)
    estado = Column(Boolean, default=True)

    carrera_id = Column(Integer, ForeignKey("carrera.id"), nullable=False)

    # Relación 1:N con Materia
    carrera = relationship("Carrera", back_populates="planes")
    materias = relationship("Materia", back_populates="plan")
