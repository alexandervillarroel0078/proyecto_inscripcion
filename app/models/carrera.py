from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Carrera(Base):
    __tablename__ = "carrera"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    
    # Relación 1:N con PlanEstudio
    planes = relationship("PlanEstudio", back_populates="carrera")