from src.core.database import database as db


class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    tipo_servicio = db.Column(db.Enum('Análisis', 'Consultoría', 'Desarrollo',name="tipo_servicio_enum"), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False)
    institucion_id = db.Column(db.Integer, db.ForeignKey('instituciones.id'))
    institucion = db.relationship("Institucion", back_populates='servicios')

    def __init__(self, nombre, descripcion, keywords, centros, tipo_servicio, habilitado, institucion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.keywords = keywords
        self.centros = centros
        self.tipo_servicio = tipo_servicio
        self.habilitado = habilitado
        self.institucion = institucion
