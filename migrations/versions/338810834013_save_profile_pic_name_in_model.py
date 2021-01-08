"""save profile pic name in model

Revision ID: 338810834013
Revises: 92523479db77
Create Date: 2021-01-08 15:05:05.805545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '338810834013'
down_revision = '92523479db77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('profile_pic', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member', 'profile_pic')
    # ### end Alembic commands ###