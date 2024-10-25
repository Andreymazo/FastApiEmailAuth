import os

from databases import Database
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
message = Table(
    "message",
    metadata,
    Column("message_id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, server_default=func.now(), nullable=False),#instead of func.now can be datetime.datetime.now or func.sysdate()
    Column("time_updated", DateTime, onupdate=func.current_timestamp(), nullable=False),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False)
)
user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("parent_message_id", Integer),
    Column("email", String(50)),
    Column("created_date", DateTime, server_default=func.now(), nullable=False),#instead of func.now can be datetime.datetime.now or func.sysdate()

    ForeignKeyConstraint(
        ["parent_message_id"], ["message.message_id"], name="fk_element_parent_element_id"
    ),
)
# databases query builder
database = Database(DATABASE_URL)