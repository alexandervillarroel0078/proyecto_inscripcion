from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Materia(Base):
    __tablename__ = "materia"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(120), nullable=False)
    creditos = Column(Integer, nullable=False)
    horas_sem = Column(Integer, nullable=False)

    # 🔑 Claves foráneas
    nivel_id = Column(Integer, ForeignKey("nivel.id"), nullable=False)
    plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)

    # Relaciones
    nivel = relationship("Nivel", back_populates="materias")
    plan = relationship("PlanEstudio", back_populates="materias")

    # 🔗 Relaciones de prerequisitos
    prerrequisitos = relationship(    "Prerequisito",    foreign_keys="[Prerequisito.materia_id]",    back_populates="materia",
    overlaps="requisitos"
   )
