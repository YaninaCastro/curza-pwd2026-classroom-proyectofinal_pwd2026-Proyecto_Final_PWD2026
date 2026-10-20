from app.controllers.mascota_controller import MascotaController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

mascotas=Blueprint ('mascotas', __name__, url_prefix='/mascotas')

@mascotas.route('/')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def get_all():
    return MascotaController.get_all()

@mascotas.route('/<id>')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def show(id:int):
    return MascotaController.show(id)

@mascotas.route('/', methods=['POST'])
@rol_access('Administrador/a', 'recepcionista')
def create():
    return MascotaController.create(request.get_json())  
                                                             
@mascotas.route('/<id>', methods=['PUT'])
@rol_access('Administrador/a', 'recepcionista')
def update(id):
    return MascotaController.update(request.get_json(), id=id)

@mascotas.route('/<id>', methods=['DELETE'])
@rol_access('Administrador/a', 'recepcionista')
def destroy(id):
    return MascotaController.destroy( id=id)