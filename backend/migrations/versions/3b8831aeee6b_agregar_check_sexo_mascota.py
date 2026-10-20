"""agregar check sexo mascota

Revision ID: 3b8831aeee6b
Revises: c30607095e53
Create Date: 2026-10-04 18:08:46.847459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b8831aeee6b'
down_revision = 'c30607095e53'
branch_labels = None
depends_on = None

def upgrade():
    op.create_check_constraint(
        'ck_mascota_sexo',
        'mascota',
        "sexo IN ('H', 'M')"
    )


def downgrade():
    op.drop_constraint(
        'ck_mascota_sexo',
        'mascota',
        type_='check'
    )