from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Nivel(Base):
    __tablename__ = "nivel"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, nullable=False)   # Ej: 1, 2, 3...
    nombre = Column(String(100), nullable=False)  # Ej: Primer Semestre

    # Relación 1:N con Materia
    materias = relationship("Materia", back_populates="nivel")
