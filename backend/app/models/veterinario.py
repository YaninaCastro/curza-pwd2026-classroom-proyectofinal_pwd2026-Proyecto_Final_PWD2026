from app.database import db
from app.models.base_model import BaseModel

class Veterinario(BaseModel):

    __tablename__= "veterinario"
    nombre=db.Column(db.String(30), nullable=False)
    apellido=db.Column(db.String(30), nullable=False)
    telefono=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(120), nullable=False)
    matricula=db.Column(db.String(20), unique=True, nullable=False)
    especialidad=db.Column(db.String(120), nullable=False)
    usuario_id=db.Column(db.Integer,db.ForeignKey('usuario.id'), unique=True, nullable=True)

    usuario=db.relationship('Usuario', backref='veterinario')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email,
            "matricula": self.matricula,
            "especialidad": self.especialidad,
            "usuario_sistema": self.usuario.usuario if self.usuario else None
        }
