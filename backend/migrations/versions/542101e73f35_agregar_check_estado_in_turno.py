"""agregar check estado in turno

Revision ID: 542101e73f35
Revises: 3b8831aeee6b
Create Date: 2026-10-04 18:17:03.125638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542101e73f35'
down_revision = '3b8831aeee6b'
branch_labels = None
depends_on = None

def upgrade():
    op.create_check_constraint(
        'ck_turno_estado',
        'turno',
        "estado IN ('pendiente', 'cancelado', 'atendido')"
    )


def downgrade():
    op.drop_constraint(
        'ck_turno_estado',
        'turno',
        type_='check'
    )