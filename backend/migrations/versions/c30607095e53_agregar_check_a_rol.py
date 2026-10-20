"""agregar check a rol

Revision ID: c30607095e53
Revises: 1fc46be80023
Create Date: 2026-10-04 17:18:02.804325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c30607095e53'
down_revision = '1fc46be80023'
branch_labels = None
depends_on = None


def upgrade():
    op.create_check_constraint(
        'ck_rol_nombre',
        'rol',
        "nombre IN ('Administrador/a', 'recepcionista', 'veterinario/a')"
    )


def downgrade():
    op.drop_constraint(
        'ck_rol_nombre',
        'rol',
        type_='check'
    )
