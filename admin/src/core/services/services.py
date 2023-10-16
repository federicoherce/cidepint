from sqlalchemy import Column, Integer, String, Enum, Boolean
from src.core.database import database as db
from datetime import datetime


class Servicio(db.Model):
    __tablename__ = "servicios"
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=False)
    keywords = Column(String(200), nullable=False)
    centros = Column(String(200), nullable=False)
    tipo_servicio = Column(Enum('Análisis', 'Consultoría', 'Desarrollo',name="tipo_servicio_enum"), nullable=False)
    habilitado = Column(Boolean, nullable=False)

    def __init__(self, nombre, descripcion, keywords, centros, tipo_servicio, habilitado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.keywords = keywords
        self.centros = centros
        self.tipo_servicio = tipo_servicio
        self.habilitado = habilitado
