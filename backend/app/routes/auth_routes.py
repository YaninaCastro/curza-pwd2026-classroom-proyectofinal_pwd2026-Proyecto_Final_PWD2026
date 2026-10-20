from app.auth.controller import AuthController
from flask import request, Blueprint
from flask_jwt_extended import jwt_required


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    return AuthController.login(request.get_json())


@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    return AuthController.refresh()



@auth.route('/me')
@jwt_required()
def me():
    return AuthController.me()