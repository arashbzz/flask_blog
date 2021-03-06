"""empty message

Revision ID: dc5276ccbce2
Revises: d10d9f189681
Create Date: 2021-07-24 00:10:47.209775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dc5276ccbce2'
down_revision = 'd10d9f189681'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('title', sa.String(length=128), nullable=False))
    op.add_column('blog', sa.Column('summery', sa.String(length=256), nullable=True))
    op.add_column('blog', sa.Column('slug', sa.String(length=128), nullable=False))
    op.drop_index('name', table_name='blog')
    op.drop_index('slung', table_name='blog')
    op.create_unique_constraint(None, 'blog', ['title'])
    op.create_unique_constraint(None, 'blog', ['slug'])
    op.drop_column('blog', 'name')
    op.drop_column('blog', 'slung')
    op.drop_column('blog', 'description')
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.add_column('blog', sa.Column('description', mysql.VARCHAR(length=256), nullable=True))
    op.add_column('blog', sa.Column('slung', mysql.VARCHAR(length=128), nullable=False))
    op.add_column('blog', sa.Column('name', mysql.VARCHAR(length=128), nullable=False))
    op.drop_constraint(None, 'blog', type_='unique')
    op.drop_constraint(None, 'blog', type_='unique')
    op.create_index('slung', 'blog', ['slung'], unique=False)
    op.create_index('name', 'blog', ['name'], unique=False)
    op.drop_column('blog', 'slug')
    op.drop_column('blog', 'summery')
    op.drop_column('blog', 'title')
    # ### end Alembic commands ###
