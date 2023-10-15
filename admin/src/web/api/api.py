from flask import Blueprint, request, jsonify
from src.core import api
from src.web.schemas.auth import auth_schema, profile_schema
from src.web.schemas.services import service_schema
from marshmallow import ValidationError
from src.core import services


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.post("/auth")
def login():
    try:
        data = auth_schema.load(request.json)
    except ValidationError:
        return jsonify({"error": "Parametros invalidos"}), 400

    if api.check_user(data['email'], data['password']):
        return jsonify({'result': 'succes'}), 200
    else:
        return jsonify({'result': 'fail'}), 400


@api_bp.get("/me/profile/<id>")
def profile(id):
    user = api.get_user_by_id(id)
    if user is None:
        return jsonify({"error": "Parametros invalidos"}), 404
    data = profile_schema.dump(user)
    return data, 200


@api_bp.get("/services/<id>")
def service(id):
    service = services.get_service(id)
    if service is None:
        return jsonify({"error": "Parametros invalidos"}), 404
    data = service_schema.dump(service)
    return data, 200
