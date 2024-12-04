"""initial migration

Revision ID: 870ea2f1574f
Revises: 
Create Date: 2024-12-05 02:16:15.633931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '870ea2f1574f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('main_menu_items', 'response',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('main_menu_items', 'response',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    # ### end Alembic commands ###