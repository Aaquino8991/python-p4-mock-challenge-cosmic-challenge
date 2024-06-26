"""implement relationships

Revision ID: cac95f086195
Revises: 1e59512c38d7
Create Date: 2024-05-12 11:07:47.138283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac95f086195'
down_revision = '1e59512c38d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scientist_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_missions_planet_id_planets'), 'planets', ['planet_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_missions_scientist_id_scientists'), 'scientists', ['scientist_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_missions_scientist_id_scientists'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_missions_planet_id_planets'), type_='foreignkey')
        batch_op.drop_column('planet_id')
        batch_op.drop_column('scientist_id')

    # ### end Alembic commands ###
