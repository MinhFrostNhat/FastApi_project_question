"""create questions table

Revision ID: aa6485e56391
Revises: ce4c9c172fe1
Create Date: 2021-05-20 15:44:27.571320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa6485e56391'
down_revision = 'ce4c9c172fe1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.VARCHAR(225)),
        sa.Column('answer_a', sa.VARCHAR(225)),
        sa.Column('answer_b', sa.VARCHAR(225)),
        sa.Column('type', sa.Integer),
        sa.Column('subject_id', sa.Integer),
        sa.Column('create_at', sa.DATETIME),

    )


def downgrade():
    pass
