import os
from databases import Database
from sqlalchemy import (
    Column,
    TIMESTAMP,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    MetaData,
    String,
    Boolean,
    Table,
    create_engine
)
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

#for localhost
DATABASE_URL = 'postgresql://postgres:123456@localhost/fast_api_email'
#for docker
# DATABASE_URL = os.getenv("DATABASE_URL")
# SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()
message = Table(
    "message",
    metadata,
    Column("message_id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", TIMESTAMP(timezone=True), server_default=func.now()),
        #    DateTime(timezone=True), server_default=func.now()),#server_default=func.now(), nullable=False),#instead of func.now can be datetime.datetime.now or func.sysdate()
    # Column("created_date", type_= TIMESTAMP(timezone=True), server_default=func.now(), nullable=False),
    Column("time_updated", TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()),
        #    DateTime(timezone=True), server_default=func.now(), onupdate=func.now()),# onupdate=func.current_timestamp(), nullable=False),
    # Column("time_updated",  type_= TIMESTAMP(timezone=True), onupdate=func.current_timestamp(), nullable=False),
     

    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False)
)
# import sqalchemy as sa

# ...

#     registered_at: datetime = Field(
#         # Add this parameter
#         sa_column=sa.Column(sa.DateTime(timezone=True), nullable=False),
#         default_factory=lambda: datetime.now(timezone.utc)
#     )
user = Table(
    "user",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("parent_message_id", Integer, nullable=True),
    Column("name", String(255)),
    Column("email", String(50), unique=True),
    Column("hashed_password", String),
    Column("is_active", Boolean, default=True),
    Column("created_date", DateTime, server_default=func.now(), nullable=False),#instead of func.now can be datetime.datetime.now or func.sysdate()

    ForeignKeyConstraint(
        ["parent_message_id"], ["message.message_id"], name="fk_element_parent_element_id"
    ),
)
# databases query builder
database = Database(DATABASE_URL)
