"""purchase date added to table

Revision ID: e3f25f45a035
Revises: 899414a27c51
Create Date: 2024-05-06 12:21:42.273794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3f25f45a035'
down_revision = '899414a27c51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('purchase_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.drop_column('purchase_date')

    # ### end Alembic commands ###
