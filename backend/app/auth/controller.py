from app.database import db
from app.models.usuario import Usuario
from flask import Response, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, create_refresh_token

class AuthController():

    @staticmethod
    def login(data:dict) -> tuple[Response, int]:
        usuario = data.get('usuario')
        password = data.get('password')

        if not usuario or not password:
            return ({'message': 'Faltan datos'}), 422

        usuario = db.session.execute(
            db.select(Usuario).filter_by(usuario=usuario)
        ).scalar_one_or_none()

        if  usuario and usuario.validate_password(password):
            access_token = create_access_token(                     #create_access_token() es la función que genera el JWT.
                identity=str(usuario.id),
                additional_claims={
                    'rol': usuario.rol.nombre}
            )
            refresh_token= create_refresh_token(
                identity=str(usuario.id)
            )

            return jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'rol': usuario.rol.nombre,
                'id': usuario.id,
                'nombre': usuario.nombre,
                'apellido': usuario.apellido
            }), 200

        return jsonify({'message': "Credenciales inválidas"}), 401


    @staticmethod
    def refresh() -> tuple[Response, int]:

        usuario_id=get_jwt_identity()

        usuario = db.session.get(Usuario, int(usuario_id))

        access_token = create_access_token(                     
            identity=str(usuario_id),
            additional_claims={
            'rol': usuario.rol.nombre
            }
        )
        return  jsonify({'access_token': access_token}), 200


    @staticmethod
    def me() -> tuple[Response, int]:
        usuario_id = get_jwt_identity()

        usuario = db.session.get(Usuario, usuario_id)

        if not usuario:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        return jsonify({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'email': usuario.email,
            'rol': usuario.rol.nombre,
            'usuario': usuario.usuario
        }), 200
