"""empty message

Revision ID: 276c78c4a2b7
Revises: 3c00080e3336
Create Date: 2022-04-18 01:54:43.631646

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '276c78c4a2b7'
down_revision = '3c00080e3336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config')
    op.drop_table('config_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config_item',
    sa.Column('sys_created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('sys_changed_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('config_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('value', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('env', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['config_id'], ['config.id'], name='config_item_config_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='config_item_pkey')
    )
    op.create_table('config',
    sa.Column('sys_created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('sys_changed_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('area', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('category', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('sub_cat', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='config_pkey')
    )
    # ### end Alembic commands ###
