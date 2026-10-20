from app.controllers.dueno_controller import DuenoController
from flask import request, Blueprint
from app.decorators.rol_access import rol_access

duenos=Blueprint ('duenos', __name__, url_prefix='/duenos')

@duenos.route('/')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def get_all():
    return DuenoController.get_all()

@duenos.route('/<id>')
@rol_access('Administrador/a', 'recepcionista','veterinario/a')
def show(id:int):
    return DuenoController.show(id)

@duenos.route('/', methods=['POST'])
@rol_access('Administrador/a', 'recepcionista')
def create():
    return DuenoController.create(request.get_json())         #request.get_json() no "transforma a JSON". Es al revés: toma el JSON recibido en la petición y lo convierte a un diccionario de Python.
                                                              #preguntar ia porque algunos son métodos y otros no, PORQUE EN GET NO SE PONE ['GET']

@duenos.route('/<id>', methods=['PUT'])
@rol_access('Administrador/a', 'recepcionista')
def update(id):
    return DuenoController.update(request.get_json(), id=id)

@duenos.route('/<id>', methods=['DELETE'])
@rol_access('Administrador/a', 'recepcionista')
def destroy(id):
    return DuenoController.destroy(id=id)

