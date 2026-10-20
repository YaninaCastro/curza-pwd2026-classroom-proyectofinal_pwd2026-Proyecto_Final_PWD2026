from flask import Flask
from app.database import db
from app.config import config

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from flask_cors import CORS

import os
migrate = Migrate()
jwt= JWTManager()

#conjunto de routes
from app.routes.dueno_route import duenos
from app.routes.mascota_route import mascotas
from app.routes.veterinario_route import veterinarios
from app.routes.turno_route import turnos
from app.routes.usuario_route import usuarios
from app.routes.rol_route import roles
from app.routes.auth_routes import auth


def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app)

    from app.models.dueno import Dueno
    from app.models.mascota import Mascota
    from app.models.veterinario import Veterinario
    from app.models.turno import Turno
    from app.models.usuario import Usuario
    from app.models.rol import Rol

    #acá írian la importación de los modelos probar antes sin importarlos haber que pasa
    app.register_blueprint(duenos)        #preguntar a la ia porque app.register_blueprint lo puedo usar de una sin importar:porque es un método de flask
    app.register_blueprint(mascotas)
    app.register_blueprint(veterinarios)
    app.register_blueprint(turnos)
    app.register_blueprint(usuarios)
    app.register_blueprint(roles)
    app.register_blueprint(auth)

    @app.route('/')
    @app.route('/<nombre>')
    def home(nombre=None):
        if nombre == None:
            return f'<h1>"Bienvenida a programación Web"</h1>'
        return f'Hola {nombre}, bienvenida a programación web'

    return app