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



class Solicitud(db.Model):
    __tablename__ = "solicitudes"
    id = db.Column(Integer, primary_key=True, unique=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey("servicios.id"))
    cliente_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    detalles = db.Column(String(500), nullable = True)
    estado = db.Column(db.String(20), nullable = False, default='EN PROCESO')  # Estados: aceptada, rechazada, en proceso, finalizada, canceladaa
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_cambio_estado = db.Column(db.DateTime, default=datetime.utcnow)
    observacion_cambio_estado = db.Column(db.String(200), default='')
    # Falta el campo de archivos adjuntos
    cliente = db.relationship('User', backref='solicitudes')
    servicio = db.relationship('Servicio', backref='solicitudes')

    def __init__(self, servicio_id, cliente_id, detalles):
        self.servicio_id = servicio_id
        self.cliente_id = cliente_id
        detalles = detalles
        
