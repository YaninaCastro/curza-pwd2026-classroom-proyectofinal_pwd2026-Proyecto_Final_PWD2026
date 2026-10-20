from flask import Response, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.controllers import Controller
from app.database import db
from app.models.mascota import Mascota

class MascotaController(Controller):                 
    @staticmethod
    def get_all() ->tuple[Response, int]:
        mascotas= Mascota.query.all()
        if len(mascotas) > 0:
            return jsonify([ d.to_dict() for d in mascotas]), 200                                      
        return  { 'message': 'No hay mascotas registradas'}      
                                                       

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        mascota=Mascota.query.get(id)
        if not mascota:
             return {"message": "la mascota no fue encontrada, volver a intentar o chequear el id"}, 404
        return jsonify([mascota.to_dict()]),200             #si no usará jsonify Flask lo transforma igual en un json


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:
        try:
            nuevo=  Mascota(
                nombre=data['nombre'],
                especie=data['especie'],
                raza=data['raza'],
                sexo=data['sexo'],
                fecha_nto=data.get('fecha_nto'),
                dueno_id=data['dueno_id']          
            )
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nueva mascota agregada con éxito', 'id': nuevo.id}, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar a la mascota, verificar que estén todos los datos y corresponda con el tipo solicitado', 'error': str(e)}, 500

    @staticmethod
    def update(data:dict, id:int) ->tuple[Response, int]:      
    
        mascota=db.session.get(Mascota,id)
        if not mascota:
            return {'message': 'mascota no encontrada, verificar id'}, 404
        
        try:
            mascota.nombre = data.get('nombre', mascota.nombre)
            mascota.especie = data.get('especie', mascota.especie)
            mascota.raza = data.get('raza', mascota.raza)
            mascota.sexo = data.get('sexo', mascota.sexo)
            mascota.fecha_nto = data.get('fecha_nto', mascota.fecha_nto)
            mascota.dueno_id = data.get('dueno_id', mascota.dueno_id)

            db.session.commit()

            return { 'message': f'los datos de la mascota {mascota.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar agregar la mascota, verificar que estén todos los datos y corresponda con el tipo solicitado','error': str(e)}, 500
   

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        mascota=db.session.get(Mascota, id)
        if not mascota:
            return {'message': 'mascota no encontrada, verificar id'}, 404
        try:
            db.session.delete(mascota)
            db.session.commit()
            return { 'message': f'la mascota {mascota.id} fue eliminada'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar la mascota, verificar id', 'error': str(e)}, 500
        

    

