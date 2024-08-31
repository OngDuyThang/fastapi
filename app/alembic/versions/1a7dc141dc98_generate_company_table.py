"""generate company table

Revision ID: 1a7dc141dc98
Revises: 
Create Date: 2024-08-27 08:57:57.113328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from constants.enums import CompanyMode


# revision identifiers, used by Alembic.
revision: str = '1a7dc141dc98'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.UUID, primary_key=True, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("mode", sa.Enum(CompanyMode), nullable=False, default=CompanyMode.OUTSOURCE),
        sa.Column("rating", sa.String, nullable=False, default=0),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table("companies")
    op.execute("DROP TYPE companymode;")