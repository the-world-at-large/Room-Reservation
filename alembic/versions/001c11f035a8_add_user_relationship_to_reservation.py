"""Add user relationship to Reservation

Revision ID: 001c11f035a8
Revises: d149248e331a
Create Date: 2024-07-04 18:16:40.491192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001c11f035a8'
down_revision = 'd149248e331a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reservation_user_id_user', 'user', ['user_id'], ['id'],
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
