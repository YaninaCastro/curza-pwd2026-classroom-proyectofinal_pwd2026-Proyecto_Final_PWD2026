from app.database import db
from app.models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(BaseModel):
    __tablename__= 'usuario'
    usuario=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String, nullable=False)
    nombre=db.Column(db.String(30), nullable=False)
    apellido=db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), unique =True, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'), nullable=False)

    rol= db.relationship('Rol', backref='usuarios')

    def to_dict(self):
        return {
        "id_usuario": self.id,
        "usuario": self.usuario,
        "nombre": self.nombre,
        "apellido": self.apellido,
        "email": self.email,
        "rol": {
            "id_rol": self.rol.id,
            "nombre_rol": self.rol.nombre
        },
        "fecha_created_at": self.created_at,
        "fecha_updated_at": self.updated_at
        }

    def validate_password(self, password:str) -> bool:
      return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
      self.password = generate_password_hash(password)