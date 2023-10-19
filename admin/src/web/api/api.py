from flask import Blueprint, request, jsonify
from src.core import api
from src.web.schemas.auth import auth_schema, profile_schema
from src.web.schemas.services import service_schema, solicitud_schema, request_show_schema
from src.web.schemas.service_type import service_type
from src.web.schemas.institutions import paginated_schema, institution_schema
from marshmallow import ValidationError
from src.core import services
from src.core import instituciones as module_institutions


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.post("/auth")
def login():
    try:
        data = auth_schema.load(request.json)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    if api.check_user(data['email'], data['password']):
        return jsonify({'result': 'success'}), 200
    else:
        return jsonify({'result': 'fail'}), 400


@api_bp.get("/me/profile/<id>")
def profile(id):
    user = api.get_user_by_id(id)
    if user is None:
        return jsonify({"error": "Parametros invalidos"}), 400
    return profile_schema.dump(user), 200


@api_bp.get("/services/<id>")
def service(id):
    service = services.get_service(id)
    if service is None:
        return jsonify({"error": "Parametros invalidos"}), 404
    data = service_schema.dump(service)
    return data, 200


@api_bp.get("/services-type")
def services_type():
    services_type_list = ["Analisis", "Consultoria", "Desarrollo"]
    return service_type.dump({"data": services_type_list}), 200


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
def get_request(id):
    request = services.show_solicitud(id)
    if request is None:
        return jsonify({"error": "Parametros invalidos"}), 400
    return request_show_schema.dump(request), 200


@api_bp.post("/me/requests")
def solicitud():
    try:
        data = request.json

        # Valida y carga los datos en el esquema
        errors = solicitud_schema.validate(data)

        services.create_solicitud(**data)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    return jsonify({'result': 'succes'}), 201
