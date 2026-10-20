from app.database import db
from app.models.base_model import  BaseModel


class Dueno(BaseModel):
    __tablename__ = "dueno"
    dni=db.Column(db.String(8), nullable=False, unique=True)
    nombre=db.Column(db.String(30), nullable=False)
    apellido=db.Column(db.String(30), nullable=False)
    telefono=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(50), unique=True)


    def to_dict(self):
        return {
            "id": self.id,
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email
        }
