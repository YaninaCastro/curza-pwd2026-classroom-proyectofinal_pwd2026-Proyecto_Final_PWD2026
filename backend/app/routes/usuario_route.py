from app.controllers.usuario_controller import UsuarioController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

usuarios=Blueprint ('usuarios', __name__, url_prefix='/usuarios')

@usuarios.route('/')
@rol_access('Administrador/a', 'recepcionista')
def get_all():
    return UsuarioController.get_all()

@usuarios.route('/<id>')
@rol_access('Administrador/a', 'recepcionista')
def show(id:int):
    return UsuarioController.show(id)

@usuarios.route('/', methods=['POST'])
@rol_access('Administrador/a')
def create():
    return UsuarioController.create(request.get_json())  
                                                             
@usuarios.route('/<id>', methods=['PUT'])
@rol_access('Administrador/a',)
def update(id):
    return UsuarioController.update(request.get_json(), id=id)

@usuarios.route('/<id>', methods=['DELETE'])
@rol_access('Administrador/a',)
def destroy(id):
    return UsuarioController.destroy(id=id)