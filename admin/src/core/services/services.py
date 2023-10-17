from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from src.core.database import database as db


class Servicio(db.Model):
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=False)
    keywords = Column(String(200), nullable=False)
    centros = Column(String(200), nullable=False)
    tipo_servicio = Column(Enum('Análisis', 'Consultoría', 'Desarrollo',name="tipo_servicio_enum"), nullable=False)
    habilitado = Column(Boolean, nullable=False)
    institucion_id = Column(Integer, ForeignKey('instituciones.id'))
    institucion = db.relationship("Institucion", back_populates='servicios')

    def __init__(self, nombre, descripcion, keywords, centros, tipo_servicio, habilitado, institucion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.keywords = keywords
        self.centros = centros
        self.tipo_servicio = tipo_servicio
        self.habilitado = habilitado
        self.institucion = institucion