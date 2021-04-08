"""empty message

Revision ID: 6b9d98ec9046
Revises: 0aab8f7d6797
Create Date: 2021-02-08 01:18:28.808706

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '6b9d98ec9046'
down_revision = '0aab8f7d6797'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sessions', sa.Column('facebook', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('github', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('gitlab', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('instagram', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('linkedin', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('twitter', sa.String(), nullable=True))
    op.add_column('sessions', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sessions', 'website')
    op.drop_column('sessions', 'twitter')
    op.drop_column('sessions', 'linkedin')
    op.drop_column('sessions', 'instagram')
    op.drop_column('sessions', 'gitlab')
    op.drop_column('sessions', 'github')
    op.drop_column('sessions', 'facebook')
    # ### end Alembic commands ###