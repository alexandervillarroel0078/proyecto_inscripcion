from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Prerequisito(Base):
    __tablename__ = "prerequisito"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(20), default="OBLIGATORIO")
    nota_min = Column(Integer, default=51)

    # Llaves foráneas
    materia_id = Column(Integer, ForeignKey("materia.id"), nullable=False)
    prerequisito_id = Column(Integer, ForeignKey("materia.id"), nullable=False)

    # Relaciones
    materia = relationship("Materia", foreign_keys=[materia_id], backref="requisitos")
    prerequisito = relationship("Materia", foreign_keys=[prerequisito_id])
