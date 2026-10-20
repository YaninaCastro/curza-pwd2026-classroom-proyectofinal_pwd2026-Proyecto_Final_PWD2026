from flask import Response, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.controllers import Controller
from app.database import db
from app.models.turno import Turno

class TurnoController(Controller):                 
    @staticmethod
    def get_all() ->tuple[Response, int]:
        turnos= Turno.query.order_by(Turno.id).all()
        if len(turnos) > 0:
            return jsonify([ d.to_dict() for d in turnos]), 200                                      
        return  { 'message': 'No hay turnos registrados'}                                                 #Podés leerla mentalmente en este orden:
                                                        #[p.to_dict() for p in productos]
                                                        #como:“Para cada p que haya en productos, quiero obtener p.to_dict().”

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        turno=Turno.query.get(id)
        if not turno:
             return {"message": "Turno no encontrado, volver a intentar o chequear el id"}, 404
        return jsonify([turno.to_dict()]),200


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:

        try:
            nuevo=  Turno(
                fecha=data['fecha'],
                hora=data['hora'],
                mascota_id=data['mascota_id'],
                veterinario_id=data['veterinario_id'],
                motivo= data['motivo'],
                estado= data['estado']
            )
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nuevo turno agregado correctamente', 'id': nuevo.id}, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar el turno, verificar que estén todos los datos y corresponda con el tipo solicitado en cada campo', 'error': str(e)}, 500

    @staticmethod
    def update(data, id:int) ->tuple[Response, int]:      
    
        turno=db.session.get(Turno,id)
        if not turno:
            return {'message': 'turno no encontrado, verificar id'}, 404
        
        try:
            turno.fecha = data.get('fecha', turno.fecha)
            turno.hora = data.get('hora', turno.hora)
            turno.mascota_id = data.get('mascota_id', turno.mascota_id)
            turno.veterinario_id = data.get('veterinario_id', turno.veterinario_id)
            turno.motivo = data.get('motivo', turno.motivo)
            turno.estado = data.get('estado', turno.estado)

            db.session.commit()

            return { 'message': f'los datos del turno {turno.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar agregar el nuevo turno verificar datos', 'error': str(e)}, 500

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        turno=db.session.get(Turno, id)
        if not turno:
            return {'message': 'turno no encontrado, verificar id'}, 404
        try:
            db.session.delete(turno)
            db.session.commit()
            return { 'message': f'el turno {turno.id} fue eliminado'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar el nuevo turno verificar id', 'error': str(e)}, 500
        

    

