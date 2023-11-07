from flask import Blueprint, request, jsonify
from src.core import api
from src.web.schemas.auth import auth_schema, profile_schema
from src.web.schemas.services import service_schema, solicitud_schema, request_show_schema
from src.web.schemas.services import solicitudes_schema, get_solicitud_schema, paginated_services
from src.web.schemas.service_type import service_type
from src.web.schemas.institutions import paginated_schema, institution_schema
from marshmallow import ValidationError
from src.core import services
from src.core import configuracion
from src.core import instituciones as module_institutions
from src.core import auth
from flask_jwt_extended import jwt_required, get_jwt_identity



api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get('/user_jwt')
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = api.get_user_by_id(current_user)
    return profile_schema.dump(user), 200


@api_bp.post("/auth")
def login():
    """
    Recibe el email y contraseña de un usuario. Si el usuario
    se encuentra registrado, retorna 'succes', de lo contrario,
    retorna 'fail'.
    """
    try:
        data = auth_schema.load(request.json)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    if api.check_user(data['email'], data['password']):
        return jsonify({'result': 'success'}), 200
    else:
        return jsonify({'result': 'fail'}), 400



@api_bp.get("/me/profile/")
@jwt_required()
def profile():
    """
    Retorna la información de un usuario a partir de su ID.
    """
    user = auth.get_user_by_id(get_jwt_identity())

    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return profile_schema.dump(user), 200


@api_bp.get("/services/<id>")
def service(id):
    if not id.isdigit():
        return jsonify({"error": "Parametros invalidos"}), 400
    service = services.get_service(id)
    if service is None:
        return jsonify({"error": "Parametros invalidos"}), 404
    data = service_schema.dump(service)
    return data, 200


@api_bp.get("/contacto")
def contacto():
    informacion = configuracion.get_info_contacto()
    return jsonify({'email': informacion.email,
                    'telefono': informacion.telefono,
                    'direccion': informacion.direccion}), 200


@api_bp.get("/all_services")
def all_services():
    services_list = services.get_all_services() 
    data = service_schema.dump(services_list, many=True)  
    return data, 200
    


@api_bp.get("/services-type")
def services_type():
    services_type_list = ["Analisis", "Consultoria", "Desarrollo"]
    return service_type.dump({"data": services_type_list}), 200


@api_bp.get("/services/search")
def search_services():
    """
    Busqueda de servicios por keywords, tipo, página y número de pagina.
    El parámetro q es obligatorio y los parámetros tipo, page y per_page opcionales
    """
    try:
        request_data = paginated_services.load(request.args)
    except ValidationError:
        return jsonify({"error": "Parámetros inválidos"}), 400

    page = request_data['page']
    per_page = request_data['per_page']
    q = request_data['q']
    tipo = request_data.get('tipo')

    list_services_paginated = (
        services.paginate_services_type_and_keywords(tipo, q, page, per_page)
        if tipo is not None
        else services.paginate_services_keyword(q, page, per_page)
    )

    serialized_services = [
        {**service_schema.dump(servicio), 'institucion': servicio.institucion.nombre}
        for servicio in list_services_paginated.items
    ]

    response_data = {
        "data": serialized_services,
        "page": page,
        "per_page": per_page,
        "total": list_services_paginated.total
    }
    return paginated_services.dump(response_data), 200



@api_bp.get("/institutions")
def institutions():
    try:
        request_data = paginated_schema.load(request.args)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    page = request_data['page']
    per_page = request_data['per_page']
    list_institutions_paginated = module_institutions.paginate_institutions_habilited(page, per_page)
    serialized_institutions = institution_schema.dump(list_institutions_paginated.items, many=True)
    response_data = {
        "data": serialized_institutions,
        "page": page,
        "per_page": per_page,
        "total": list_institutions_paginated.total
    }

    return paginated_schema.dump(response_data), 200


@api_bp.get("/me/requests/<id>")
@jwt_required()
def get_request(id):
    if not id.isdigit():
        return jsonify({"error": "Parametros invalidos"}), 400
    request = services.solicitudes_api_id(get_jwt_identity(),id)
    if request is None:
        return jsonify({"error": "No le pertence ninguna solicitud con ese id"}), 400
    return request_show_schema.dump(request), 200


@api_bp.post("/me/requests")
@jwt_required()
def solicitud():
    try:
        data = request.json
        data['cliente_id'] = get_jwt_identity()

        errors = solicitud_schema.validate(data)

        solicitud = services.create_solicitud(**data)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    return jsonify({'id': solicitud.id, 'detalles': solicitud.detalles, 'fecha de creacion': solicitud.fecha_creacion, 'estado': solicitud.estado}), 201


@api_bp.post("/me/requests/<id>/notes")
@jwt_required()
def comentar_solicitud(id):
    try:
        solicitud = services.show_solicitud(id)
        data = request.json
        comentario = data.get('comentario', '') 
        services.update_solicitud(solicitud, comentario=comentario)
        services.update_solicitud(solicitud, comentario=comentario)
    except ValidationError as err:
        print(err.messages)  
        print(err.valid_data) 
        return jsonify({"error": "Parametros invalidos"}), 400

    return jsonify({'id': solicitud.id, 'comentario': solicitud.comentario}), 201


@api_bp.get("/me/requests")
@jwt_required()
def solicitudes():
    try:
        request_data = solicitudes_schema.load(request.args)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    page = request_data['page']
    per_page = request_data['per_page']
    solicitudes_paginadas = services.paginate_solicitudes_api_id(page, per_page, get_jwt_identity())
    solicitudes_serializadas = get_solicitud_schema.dump(solicitudes_paginadas.items, many=True)
    response_data = {
        "data": solicitudes_serializadas,
        "page": page,
        "per_page": per_page,
        "total": solicitudes_paginadas.total
    }

    return solicitudes_schema.dump(response_data), 200
