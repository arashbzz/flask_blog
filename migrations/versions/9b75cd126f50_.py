"""empty message

Revision ID: 9b75cd126f50
Revises: 404feae0d4f5
Create Date: 2021-07-24 11:00:33.352414

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b75cd126f50'
down_revision = '404feae0d4f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'blog', ['title'])
    op.create_unique_constraint(None, 'blog', ['slug'])
    op.drop_column('blog', 'slung')
    op.drop_column('blog', 'name')
    op.drop_column('blog', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('description', mysql.VARCHAR(length=256), nullable=True))
    op.add_column('blog', sa.Column('name', mysql.VARCHAR(length=128), nullable=False))
    op.add_column('blog', sa.Column('slung', mysql.VARCHAR(length=128), nullable=False))
    op.drop_constraint(None, 'blog', type_='unique')
    op.drop_constraint(None, 'blog', type_='unique')
    # ### end Alembic commands ###
