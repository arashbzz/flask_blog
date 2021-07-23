"""empty message

Revision ID: ebd24fe6e034
Revises: dc5276ccbce2
Create Date: 2021-07-24 00:16:45.324791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ebd24fe6e034'
down_revision = 'dc5276ccbce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'blog', ['title'])
    op.create_unique_constraint(None, 'blog', ['slug'])
    op.drop_column('blog', 'name')
    op.drop_column('blog', 'description')
    op.drop_column('blog', 'slung')
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.add_column('blog', sa.Column('slung', mysql.VARCHAR(length=128), nullable=False))
    op.add_column('blog', sa.Column('description', mysql.VARCHAR(length=256), nullable=True))
    op.add_column('blog', sa.Column('name', mysql.VARCHAR(length=128), nullable=False))
    op.drop_constraint(None, 'blog', type_='unique')
    op.drop_constraint(None, 'blog', type_='unique')
    # ### end Alembic commands ###