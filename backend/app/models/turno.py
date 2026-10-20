from app.database import db
from app.models.base_model import BaseModel

class Turno(BaseModel):
    __tablename__= 'turno'
    fecha=db.Column(db.Date, nullable=False)
    hora=db.Column(db.Time, nullable=False)
    mascota_id=db.Column(db.Integer, db.ForeignKey('mascota.id'), nullable=False)
    veterinario_id=db.Column(db.Integer, db.ForeignKey('veterinario.id'), nullable=False)
    motivo=db.Column(db.String(200), nullable=False)
    estado=db.Column(db.String(20), db.CheckConstraint ("estado IN ('pendiente','cancelado','atendido')",  name="ck_turno_estado"), nullable=False)

    mascota=db.relationship('Mascota', backref='turnos')
    veterinario=db.relationship('Veterinario', backref='turnos')

    def to_dict(self):
        return {
        "id": self.id,
        "fecha": self.fecha.strftime("%Y-%m-%d") if self.fecha else None,
        "hora": self.hora.strftime("%H:%M") if self.hora else None,
        "mascota":{"mascota_id": self.mascota.id, "nombre": self.mascota.nombre},
        "veterinario": {"veterinario_id": self.veterinario_id, "apellido": self.veterinario.apellido, "nombre": self.veterinario.nombre},
        "motivo": self.motivo,
        "estado": self.estado
        }
