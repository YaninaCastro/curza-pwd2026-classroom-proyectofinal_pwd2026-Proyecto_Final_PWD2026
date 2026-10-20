from app.database import db
from app.models.base_model import BaseModel

class Mascota(BaseModel):

    __tablename__= "mascota"
    nombre=db.Column(db.String(30), nullable=False)
    especie=db.Column(db.String(30), nullable=False)
    raza=db.Column(db.String(50), nullable=False)
    sexo=db.Column(db.String(1), db.CheckConstraint ("sexo IN ('H','M')",  name="ck_mascota_sexo"), nullable=False)
    fecha_nto=db.Column(db.Date)
    dueno_id=db.Column(db.Integer, db.ForeignKey('dueno.id'), nullable=False)

    dueno=db.relationship("Dueno", backref="mascotas")
    
    def to_dict(self):
       return {
        "id": self.id,
        "nombre": self.nombre,
        "especie": self.especie,
        "raza": self.raza,
        "sexo": self.sexo,
        "fecha_nto": self.fecha_nto.strftime("%Y-%m-%d") if self.fecha_nto else None,
        "dueño":{"id": self.dueno.id, "nombre": self.dueno.nombre, "apellido": self.dueno.apellido}
}