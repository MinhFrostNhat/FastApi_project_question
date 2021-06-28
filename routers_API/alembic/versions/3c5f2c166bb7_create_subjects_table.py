"""create subjects table

Revision ID: 3c5f2c166bb7
Revises: 27bae11888cb
Create Date: 2021-05-20 15:47:14.584194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c5f2c166bb7'
down_revision = '27bae11888cb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subjects',
        sa.Column('id',sa.Integer, primary_key=True, index=True),
        sa.Column('title',sa.VARCHAR(225)),
        sa.Column('create_at',sa.DATETIME)
    )


def downgrade():
    pass
