"""create UserInfo table

Revision ID: 0db6c3f5df71
Revises: aa6485e56391
Create Date: 2021-05-20 15:44:58.497772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db6c3f5df71'
down_revision = 'aa6485e56391'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_info',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String(225), unique=True),
        sa.Column('password', sa.String(225)),
        sa.Column('fullname', sa.String(225), unique=True)
    )


def downgrade():
    pass
