from app.controllers.turno_controller import TurnoController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

turnos=Blueprint ('turnos', __name__, url_prefix='/turnos')

@turnos.route('/')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def get_all():
    return TurnoController.get_all()

@turnos.route('/<id>')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def show(id:int):
    return TurnoController.show(id)

@turnos.route('/', methods=['POST'])
@rol_access('Administrador/a', 'recepcionista')
def create():
    return TurnoController.create(request.get_json())  
                                                             
@turnos.route('/<id>', methods=['PUT'])
@rol_access('Administrador/a', 'recepcionista')
def update(id):
    return TurnoController.update(request.get_json(), id=id)

@turnos.route('/<id>', methods=['DELETE'])
@rol_access('Administrador/a', 'recepcionista')
def destroy(id):
    return TurnoController.destroy(id=id)