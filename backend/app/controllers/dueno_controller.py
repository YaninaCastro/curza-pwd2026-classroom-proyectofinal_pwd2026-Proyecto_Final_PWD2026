from flask import Response, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.controllers import Controller
from app.database import db
from app.models.dueno import Dueno

class DuenoController(Controller):                 
    @staticmethod
    def get_all() ->tuple[Response, int]:
        
        duenos= Dueno.query.all()
        if len(duenos) > 0:
            return jsonify([ d.to_dict() for d in duenos]), 200                                      
        return  { 'message': 'No hay dueños registrados'}                                               #Se puede leer:
                                                        #[p.to_dict() for p in productos]
                                                        #como:“Para cada p que haya en productos, quiero obtener p.to_dict().”

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        dueno=Dueno.query.get(id)
        if not dueno:
             return {"message": "Dueño no encontrado, volver a intentar o chequear el id"}, 404
        return jsonify([dueno.to_dict()]),200


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:
        try:
            nuevo=  Dueno(
                dni= data['dni'],
                nombre=data['nombre'],
                apellido=data['apellido'],
                telefono=data['telefono'],
                email=data.get('email')       #.get: Es una función/método de los diccionarios de Python que estás usando sobre data, y data viene de Flask porque request.get_json() te entrega los datos del JSON.
            )
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nuevo dueño agregado correctamente', 'id': nuevo.id}, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar el nuevo dueño/a, verificar que estén todos los datos y corresponda con el tipo solicitado en cada campo', 'error': str(e)}, 500

    @staticmethod
    def update(data:dict, id:int) ->tuple[Response, int]:      
    
        dueno=db.session.get(Dueno,id)
        if not dueno:
            return {'message': 'dueño/a no encontrado, verificar id'}, 404
        
        try:
            dueno.dni = data.get('dni', dueno.dni)
            dueno.nombre = data.get('nombre', dueno.nombre)
            dueno.apellido = data.get('apellido', dueno.apellido)
            dueno.telefono = data.get('telefono', dueno.telefono)
            dueno.email = data.get('email', dueno.email)

            db.session.commit()

            return { 'message': f'los datos del dueño {dueno.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar agregar el nuevo dueño/a verificar que estén todos los datos y correspondan al tipo de dato requerido de cada campo', 'error': str(e)}, 500

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        dueno=db.session.get(Dueno, id)
        if not dueno:
            return {'message': 'dueño/a no encontrado, verificar id'}, 404
        try:
            db.session.delete(dueno)
            db.session.commit()
            return { 'message': f'el dueño/a {dueno.id} fue eliminado'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar el nuevo dueño/a, por favor verificar id', 'error': str(e)}, 500
        

    

