"""create home table

Revision ID: 0c5d750a8682
Revises: b876f3166f6b
Create Date: 2021-10-09 00:20:35.235121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c5d750a8682'
down_revision = 'b876f3166f6b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('string',
                    sa.Column('id_string', sa.Integer(), nullable=False),
                    sa.Column('input', sa.VARCHAR(length=50), nullable=True),
                    sa.Column('last_modified', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id_string')
                    )

    op.create_table('integer',
                    sa.Column('id_integer', sa.Integer(), nullable=False),
                    sa.Column('input', sa.VARCHAR(length=50), nullable=True),
                    sa.Column('last_modified', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id_integer')
                    )


def downgrade():
    op.drop_table('string')
    op.drop_table('integer')
