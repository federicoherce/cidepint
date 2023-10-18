from marshmallow import Schema, fields


class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str()
    descripcion = fields.Str()
    keywords = fields.Str()
    centros = fields.Str()
    habilitado = fields.Boolean()


service_schema = ServiceSchema()

class SolicitudSchema(Schema):
    cliente_id = fields.Int()
    servicio_id = fields.Str()
    detalles = fields.Str()

solicitud_schema = SolicitudSchema()
