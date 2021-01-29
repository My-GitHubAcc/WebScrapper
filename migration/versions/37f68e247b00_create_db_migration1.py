"""create db_migration1

Revision ID: 37f68e247b00
Revises: 
Create Date: 2021-01-02 17:13:10.354076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f68e247b00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categorie',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
     
    )
    op.create_table(
        'form',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'gender',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'marque',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'material_fond',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'material_front',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'structure',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'taille_lunettes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'taille_temple',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.create_table(
        'lunettes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('categorie_id', sa.Integer, sa.ForeignKey('categorie.id')),
        sa.Column('form_id', sa.Integer, sa.ForeignKey('form.id')),
        sa.Column('gender_id', sa.Integer, sa.ForeignKey('gender.id')),
        sa.Column('marque_id', sa.Integer, sa.ForeignKey('marque.id')),
        sa.Column('material_fond_id', sa.Integer, sa.ForeignKey('material_fond.id')),
        sa.Column('material_front_id', sa.Integer, sa.ForeignKey('material_front.id')),
        sa.Column('structure_id', sa.Integer, sa.ForeignKey('structure.id')),
        sa.Column('taille_temple_id', sa.Integer, sa.ForeignKey('categorie.id')),
    )

def downgrade():
    op.drop_table('lunettes')
    op.drop_table('categorie')
    op.drop_table('form')
    op.drop_table('gender')
    op.drop_table('marque')
    op.drop_table('material_fond')
    op.drop_table('material_front')
    op.drop_table('structure')
    op.drop_table('taille_lunettes')
    op.drop_table('taille_temple')