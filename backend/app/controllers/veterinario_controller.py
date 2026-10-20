from flask import Response, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.controllers import Controller
from app.database import db
from app.models.veterinario import Veterinario

class VeterinarioController(Controller):                 
    @staticmethod
    def get_all() ->tuple[Response, int]:
        veterinarios= Veterinario.query.all()
        if len(veterinarios) > 0:
            return jsonify([ d.to_dict() for d in veterinarios]), 200                                      
        return  { 'message': 'No hay veterinarios registrados'}                                                #Podés leerla mentalmente en este orden:
                                                        #[p.to_dict() for p in productos]
                                                        #como:“Para cada p que haya en productos, quiero obtener p.to_dict().”

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        veterinario=Veterinario.query.get(id)
        if not veterinario:
             return {"message": "Veterinario/a no encontrado, volver a intentar o chequear el id"}, 404
        return jsonify([veterinario.to_dict()]),200


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:
        try:
            nuevo=  Veterinario(
                nombre=data['nombre'],
                apellido=data['apellido'],
                telefono=data['telefono'],
                email=data['email'],
                matricula=data['matricula'],
                especialidad= data['especialidad']
            )
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nuevo veterinario/a agregado correctamente', 'id': nuevo.id}, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar el nuevo veterinario/a, verificar que estén todos los datos y corresponda con el tipo solicitado en cada campo', 'error': str(e)}, 500

    @staticmethod
    def update(data, id:int) ->tuple[Response, int]:      
    
        veterinario=db.session.get(Veterinario,id)
        if not veterinario:
            return {'message': 'veterinario no encontrado, verificar id'}, 404
        
        try:
            veterinario.nombre = data.get('nombre', veterinario.nombre)
            veterinario.apellido = data.get('apellido', veterinario.apellido)
            veterinario.telefono = data.get('telefono', veterinario.telefono)
            veterinario.email = data.get('email', veterinario.email)
            veterinario.matricula = data.get('matricula', veterinario.matricula)
            veterinario.especialidad = data.get('especialidad', veterinario.especialidad)

            db.session.commit()

            return { 'message': f'los datos del veterinario {veterinario.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar agregar el nuevo veterinario/a verificar datos', 'error': str(e)}, 500

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        veterinario=db.session.get(Veterinario, id)
        if not veterinario:
            return {'message': 'veterinario/a no encontrado, verificar id'}, 404
        try:
            db.session.delete(veterinario)
            db.session.commit()
            return { 'message': f'el veterinario/a {veterinario.id} fue eliminado'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar el nuevo veterinario verificar id o si está en un turno pendiente', 'error': str(e)}, 500
        

    

