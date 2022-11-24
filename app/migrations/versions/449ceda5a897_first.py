"""“first”

Revision ID: 449ceda5a897
Revises: 
Create Date: 2022-11-18 00:52:47.484086

"""
import geoalchemy2
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '449ceda5a897'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apartments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('geopos', geoalchemy2.types.Geography(geometry_type='POINT', from_text='ST_GeogFromText', name='geography'), nullable=False),
    sa.Column('apartments', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apartments_id'), 'apartments', ['id'], unique=True)
    # op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_index(op.f('ix_apartments_id'), table_name='apartments')
    op.drop_table('apartments')
    # ### end Alembic commands ###
