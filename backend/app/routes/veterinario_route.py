from app.controllers.veterinario_controller import VeterinarioController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

veterinarios=Blueprint ('veterinarios', __name__, url_prefix='/veterinarios')

@veterinarios.route('/')
@rol_access('Administrador/a', 'recepcionista')
def get_all():
    return VeterinarioController.get_all()

@veterinarios.route('/<id>')
@rol_access('Administrador/a', 'recepcionista')
def show(id:int):
    return VeterinarioController.show(id)

@veterinarios.route('/', methods=['POST'])
@rol_access('Administrador/a', 'recepcionista')
def create():
    return VeterinarioController.create(request.get_json())  
                                                             
@veterinarios.route('/<id>', methods=['PUT'])
@rol_access('Administrador/a', 'recepcionista')
def update(id):
    return VeterinarioController.update(request.get_json(), id=id)

@veterinarios.route('/<id>', methods=['DELETE'])
@rol_access('Administrador/a', 'recepcionista')
def destroy(id):
    return VeterinarioController.destroy(id=id)