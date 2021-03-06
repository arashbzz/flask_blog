"""empty message

Revision ID: 3b9250c36f7a
Revises: 7c6eca35f47d
Create Date: 2021-07-13 20:43:26.944293

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b9250c36f7a'
down_revision = '7c6eca35f47d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('role', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('full_name', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.drop_table('users')
    # ### end Alembic commands ###
