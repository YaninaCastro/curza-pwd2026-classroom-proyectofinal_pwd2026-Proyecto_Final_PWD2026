from flask import Response, request, jsonify
from sqlalchemy.exc import IntegrityError

from app.controllers import Controller
from app.database import db
from app.models.usuario import Usuario

class UsuarioController(Controller):                 
    @staticmethod
    def get_all() ->tuple[Response, int]:
        usuarios= Usuario.query.all()
        if len(usuarios) > 0:
            return jsonify([ d.to_dict() for d in usuarios]), 200                                      
        return  { 'message': 'No hay usuarios registrados'}                                               #Podés leerla mentalmente en este orden:
                                                                                                        #[p.to_dict() for p in productos]
                                                                                                        #como:“Para cada p que haya en productos, quiero obtener p.to_dict().”

    @staticmethod
    def show(id:int) ->tuple[Response, int]:
        usuario=Usuario.query.get(id)
        if not usuario:
             return {"message": "Usuario/a no encontrado, volver a intentar o chequear el id"}, 404
        return jsonify([usuario.to_dict()]),200


    @staticmethod
    def create(data:dict) ->tuple[Response, int]:
        try:
            nuevo=  Usuario(
                usuario=data['usuario'],
                password=data['password'],
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                rol_id=data['rol_id']
            )

            nuevo.generate_password(nuevo.password)
            db.session.add(nuevo)
            db.session.commit()
            return { 'message': 'nuevo usuario/a agregado correctamente', 'id': nuevo.id, 'rol': nuevo.rol.nombre}, 201 
        except Exception as e:
            db.session.rollback()
            return {'message': 'Error al intentar agregar el nuevo usuario/a, verificar que estén todos los datos y corresponda con el tipo de dato solicitado en cada campo', 'error': str(e)}, 500

    @staticmethod
    def update(data, id:int) ->tuple[Response, int]:      
    
        usuario=db.session.get(Usuario,id)
        if not usuario:
            return {'message': 'usuario/a no encontrado, verificar id'}, 404
        
        try:
            usuario.usuario = data.get('usuario', usuario.usuario)
            if 'password' in data:
                usuario.generate_password(data['password'])
            usuario.nombre = data.get('nombre', usuario.nombre)
            usuario.apellido = data.get('apellido', usuario.apellido)
            usuario.email = data.get('email', usuario.email)
            usuario.rol_id = data.get('rol_id', usuario.rol_id)
          
            db.session.commit()

            return { 'message': f'los datos del usuario/a {usuario.id} fueron actualizados con éxito'}, 200
        
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar agregar el nuevo usuario/a verificar datos', 'error': str(e)}, 500

        
    @staticmethod
    def destroy(id:int)->tuple[Response, int]:
        usuario=db.session.get(Usuario, id)
        if not usuario:
            return {'message': 'usuario/a no encontrado, verificar id'}, 404
        try:
            db.session.delete(usuario)
            db.session.commit()
            return { 'message': f'el usuario/a {usuario.id} fue eliminado'}, 200
        except Exception as e:
            db.session.rollback()
            return { 'message': 'Error al intentar eliminar el nuevo usuario/a verificar id', 'error': str(e)}, 500
        

    

