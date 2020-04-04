"""empty message

Revision ID: 6c1fa3d9287d
Revises: 
Create Date: 2020-04-04 11:50:32.327290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c1fa3d9287d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loading', sa.Column('loading', sa.String(), nullable=True))
    op.alter_column('loading', 'loading_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('loading', 'loading_kpa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loading', sa.Column('loading_kpa', sa.NUMERIC(), autoincrement=False, nullable=False))
    op.alter_column('loading', 'loading_type',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_column('loading', 'loading')
    # ### end Alembic commands ###
