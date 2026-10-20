from app.controllers.rol_controller import RolController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

roles = Blueprint('roles', __name__, url_prefix='/roles')

@roles.route('/')
@rol_access('Administrador/a', 'recepcionista')
def get_all():
    return RolController.get_all()

@roles.route('/<id>')
@rol_access('Administrador/a', 'recepcionista')
def show(id):
    return RolController.show(id)

@roles.route("/", methods=['POST'])
@rol_access('Administrador/a')
def create():
    return RolController.create(request.get_json())

@roles.route("/<int:id>", methods=['PUT'])
@rol_access('Administrador/a')
def update(id):
    return  RolController.update(request.get_json(), id=id)
    

@roles.route("/<int:id>", methods=['DELETE'])
@rol_access('Administrador/a')
def destroy(id):
    return RolController.destroy(id)