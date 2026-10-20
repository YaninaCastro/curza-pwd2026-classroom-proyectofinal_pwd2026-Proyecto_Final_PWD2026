from app.database import db
from app.models.base_model import BaseModel

class Rol(BaseModel):
    __tablename__="rol"
    nombre = db.Column(db.String(20), db.CheckConstraint (
        "nombre IN ('Administrador/a','recepcionista','veterinario/a')", name="ck_rol_nombre"),
          unique=True, nullable=False)
    activo = db.Column(db.String(1), default = 'S', nullable=False)
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'activo': self.activo,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


