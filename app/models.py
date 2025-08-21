# from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, SmallInteger, UniqueConstraint
# from sqlalchemy.orm import relationship
# from .database import Base

# # ================== CARRERA ==================
# class Carrera(Base):
#     __tablename__ = "carrera"
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String(120), nullable=False, unique=True)
#     planes = relationship("PlanEstudio", back_populates="carrera")

# # ================== PLAN DE ESTUDIO ==================
# class PlanEstudio(Base):
#     __tablename__ = "plan_estudio"
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String(120), nullable=False)
#     año = Column(String(20), nullable=False)
#     vigente_desde = Column(Date, nullable=True)
#     estado = Column(Boolean, default=True)

#     carrera_id = Column(Integer, ForeignKey("carrera.id"), nullable=False)
#     carrera = relationship("Carrera", back_populates="planes")

#     materias = relationship("Materia", back_populates="plan")

# # ================== NIVEL ==================
# class Nivel(Base):
#     __tablename__ = "nivel"
#     id = Column(Integer, primary_key=True)
#     numero = Column(SmallInteger, nullable=False)
#     nombre = Column(String(120), nullable=False)
#     materias = relationship("Materia", back_populates="nivel")

# # ================== MATERIA ==================
# class Materia(Base):
#     __tablename__ = "materia"
#     id = Column(Integer, primary_key=True)
#     codigo = Column(String(20), nullable=False, unique=True, index=True)
#     nombre = Column(String(120), nullable=False, index=True)
#     creditos = Column(Integer, nullable=False)
#     estado = Column(Boolean, default=True)

#     plan_id = Column(Integer, ForeignKey("plan_estudio.id"), nullable=False)
#     plan = relationship("PlanEstudio", back_populates="materias")

#     nivel_id = Column(Integer, ForeignKey("nivel.id"), nullable=False)
#     nivel = relationship("Nivel", back_populates="materias")

#     prerrequisitos = relationship(
#         "Materia",
#         secondary="materia_prerrequisito",
#         primaryjoin="Materia.id==MateriaPrerequisito.materia_id",
#         secondaryjoin="Materia.id==MateriaPrerequisito.prerrequisito_id",
#         backref="desbloquea"
#     )

# # ================== PRERREQUISITOS ==================
# class MateriaPrerequisito(Base):
#     __tablename__ = "materia_prerrequisito"
#     id = Column(Integer, primary_key=True)
#     materia_id = Column(Integer, ForeignKey("materia.id", ondelete="CASCADE"), nullable=False)
#     prerrequisito_id = Column(Integer, ForeignKey("materia.id", ondelete="RESTRICT"), nullable=False)
#     nota_min = Column(SmallInteger, default=51)

#     __table_args__ = (UniqueConstraint("materia_id", "prerrequisito_id", name="uq_materia_prerrequisito"),)



# docker-compose down -v     
# docker-compose up --build
