from marshmallow import Schema, fields, validate


class ServiceSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str()
    descripcion = fields.Str()
    tipo_servicio = fields.Str(validate=validate.OneOf(['Análisis', 'Desarrollo', 'Consultoría']))
    keywords = fields.Str()
    habilitado = fields.Boolean()
    institucion_id = fields.Int()


service_schema = ServiceSchema()


class PaginatedServicesSchema(Schema):
    data = fields.Nested(ServiceSchema, many=True)
    q = fields.Str(required=True)
    tipo = fields.Str(validate=validate.OneOf(['Análisis', 'Desarrollo', 'Consultoría']))
    page = fields.Integer(validate=validate.Range(min=1), missing=1)
    per_page = fields.Integer(validate=validate.Range(min=1, max=10), missing=1)
    total = fields.Integer()

paginated_services = PaginatedServicesSchema()

class SolicitudSchema(Schema):
    cliente_id = fields.Int()
    servicio_id = fields.Str()
    detalles = fields.Str()
    estado = fields.Str()
    fecha_creacion = fields.Str()


solicitud_schema = SolicitudSchema(exclude=['fecha_creacion', 'estado'])
get_solicitud_schema = SolicitudSchema()


class PaginatedSolicitudesSchema(Schema):
    data = fields.Nested(SolicitudSchema, many=True)
    page = fields.Integer(validate=validate.Range(min=1), missing=1)
    per_page = fields.Integer(validate=validate.Range(min=1, max=10), missing=1)
    total = fields.Integer()

solicitudes_schema = PaginatedSolicitudesSchema()


class RequestShowSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha_creacion = fields.Date()
    fecha_cambio_estado = fields.Date()
    estado = fields.Str()
    detalles = fields.Str()


request_show_schema = RequestShowSchema()
