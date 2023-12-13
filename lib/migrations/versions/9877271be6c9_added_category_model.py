"""Added Category model

Revision ID: 9877271be6c9
Revises: 7b68ecd09334
Create Date: 2023-12-13 19:09:24.994062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9877271be6c9'
down_revision = '7b68ecd09334'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###
