"""add stripe columns to purchase table

Revision ID: 39815abee173
Revises: 4971f0f1ae00
Create Date: 2024-04-30 13:28:39.809619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39815abee173'
down_revision = '4971f0f1ae00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stripe_payment_intent_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('stripe_customer_id', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_column('stripe_customer_id')
        batch_op.drop_column('stripe_payment_intent_id')

    # ### end Alembic commands ###