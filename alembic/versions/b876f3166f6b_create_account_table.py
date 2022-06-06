"""create account table

Revision ID: b876f3166f6b
Revises: 
Create Date: 2021-10-08 14:22:41.400086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b876f3166f6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id_user', sa.Integer(), nullable=False),
                    sa.Column('username', sa.VARCHAR(
                        length=50), nullable=True),
                    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
                    sa.Column('password', sa.String(
                        length=128), nullable=True),
                    sa.Column('last_modified', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id_user')
                    )


def downgrade():
    op.drop_table('user')
