"""create result table

Revision ID: 3aa81c3670b9
Revises: 0db6c3f5df71
Create Date: 2021-05-20 15:46:52.136003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa81c3670b9'
down_revision = '0db6c3f5df71'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'result',
        sa.Column('id',sa.Integer, primary_key=True, index=True),
        sa.Column('subject_id',sa.Integer),
        sa.Column('cadidates_id',sa.Integer),
        sa.Column('answer_result',sa.VARCHAR(2000)),
        sa.Column('create_at',sa.DATETIME),

    )


def downgrade():
    pass
