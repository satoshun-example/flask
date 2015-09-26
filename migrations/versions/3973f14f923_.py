"""empty message

Revision ID: 3973f14f923
Revises: None
Create Date: 2015-09-26 07:02:52.774924

"""

# revision identifiers, used by Alembic.
revision = '3973f14f923'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table('users')
