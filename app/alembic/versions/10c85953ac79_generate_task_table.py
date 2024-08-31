"""generate task table

Revision ID: 2d51a4009e8f
Revises: 6b7baa502dd1
Create Date: 2024-08-26 11:16:22.672186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from constants.enums import TaskPriority, TaskStatus


# revision identifiers, used by Alembic.
revision: str = '10c85953ac79'
down_revision: Union[str, None] = '682a88b69b35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.UUID, primary_key=True, nullable=False),
        sa.Column("summary", sa.String, nullable=True),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("status", sa.Enum(TaskStatus), nullable=False, default=TaskStatus.BACKLOG),
        sa.Column("priority", sa.Enum(TaskPriority), nullable=False, default=TaskPriority.LOW),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    
    op.add_column("tasks", sa.Column("owner_id", sa.UUID, nullable=True))
    op.create_foreign_key("fk_task_owner", "tasks", "users", ["owner_id"],['id'])

def downgrade() -> None:
    op.drop_column("tasks", "owner_id")
    op.drop_table("tasks")
    op.execute("DROP TYPE taskstatus;")
    op.execute("DROP TYPE taskpriority;")
