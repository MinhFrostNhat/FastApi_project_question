"""create candidates table

Revision ID: 27bae11888cb
Revises: 3aa81c3670b9
Create Date: 2021-05-20 15:47:02.669007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27bae11888cb'
down_revision = '3aa81c3670b9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'candidates',
        sa.Column('id',sa.Integer, primary_key=True, index=True),
        sa.Column('name',sa.VARCHAR(225)),
        sa.Column('email',sa.VARCHAR(225)),
        sa.Column('DOB',sa.DATE),
        sa.Column('position',sa.VARCHAR(225)),
        sa.Column('create_at',sa.DATETIME)
    )


def downgrade():
    pass
