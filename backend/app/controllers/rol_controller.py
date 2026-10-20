from sqlalchemy.exc import IntegrityError
from app.models.rol import Rol
from app.database import db
from flask import Response, jsonify
from app.controllers import Controller

class RolController (Controller):
    
    @staticmethod
    def get_all() ->tuple[Response, int]:
        
        roles= Rol.query.all()
        if len(roles) > 0:
            return jsonify([ r.to_dict() for r in roles]), 200                                      
        return  { 'message': 'No hay roles  registrados'}                                               #Se puede leer:
                                                        #[p.to_dict() for p in productos]
                                                        #como:“Para cada p que haya en productos, quiero obtener p.to_dict().”

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        rol=Rol.query.get(id)
        if not rol:
             return {"message": "Rol no encontrado, volver a intentar o chequear el id"}, 404
        return jsonify([rol.to_dict()]),200


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:
        try:
            nuevo=  Rol(
                nombre=data['nombre'],
                activo=data.get('activo', 'S').upper()
            )
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nuevo rol agregado con éxito', 'id': nuevo.id}, 201 

        except IntegrityError as e:
            db.session.rollback()
            return {
            'message': 'El nombre del rol no es válido o ya existe'}, 400
        
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar el rol', 'error': str(e)}, 500

    @staticmethod
    def update(data:dict, id:int) ->tuple[Response, int]:      
    
        rol=db.session.get(Rol,id)
        if not rol:
            return {'message': 'Rol no encontrado, verificar id'}, 404
        
        try:
            rol.nombre = data.get('nombre', rol.nombre)
            rol.activo = data.get('activo', rol.activo)
            db.session.commit()

            return { 'message': f'los datos del rol {rol.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar editar el rol verificar datos y su tipo', 'error': str(e)}, 500

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        rol=db.session.get(Rol, id)
        if not rol:
            return {'message': 'rol no encontrado, verificar id'}, 404
        try:
            db.session.delete(rol)
            db.session.commit()
            return { 'message': f'el rol {rol.id} fue eliminado'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar el rol, por favor verificar id', 'error': str(e)}, 500
        
