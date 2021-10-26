"""Added user

Revision ID: 6a1ae139558e
Revises: 
Create Date: 2021-06-03 12:54:23.473847

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6a1ae139558e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=True),
    sa.Column('surname', sa.String(length=15), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('phone', sa.String(length=18), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###