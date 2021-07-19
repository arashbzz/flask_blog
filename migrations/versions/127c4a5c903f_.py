"""empty message

Revision ID: 127c4a5c903f
Revises: 7c695b54a778
Create Date: 2021-07-19 15:58:01.653904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127c4a5c903f'
down_revision = '7c695b54a778'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('slung', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slung')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('slung', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slung')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    op.drop_table('blog')
    # ### end Alembic commands ###