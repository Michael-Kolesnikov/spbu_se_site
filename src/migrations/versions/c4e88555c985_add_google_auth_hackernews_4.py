"""Add google auth + hackernews 4

Revision ID: c4e88555c985
Revises: 
Create Date: 2022-01-19 17:54:30.755371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4e88555c985'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1024), nullable=False),
    sa.Column('description', sa.String(length=2048), nullable=True),
    sa.Column('amount', sa.String(length=2048), nullable=False),
    sa.Column('submission', sa.String(length=2048), nullable=False),
    sa.Column('contacts', sa.String(length=2048), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=2048), nullable=False),
    sa.Column('uri', sa.String(length=1024), nullable=True),
    sa.Column('domain', sa.String(length=512), nullable=True),
    sa.Column('text', sa.String(length=4096), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_on', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('rank', sa.Float(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_vote',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('upvote', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_vote')
    op.drop_table('posts')
    op.drop_table('grants')
    # ### end Alembic commands ###
