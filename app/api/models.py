# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# Base  = declarative_base()

# class Message(Base):
#     __tablename__ = 'message'
#     id  = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
#     time_updated = Column(DateTime(timezone=True), onupdate=func.now())
#     user_id = Column(Integer, ForeignKey('user.user_id'))

#     author = relationship('User')


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), unique=True, index=True)
#     email = Column(String, unique=True, nullable=False)
#     age = Column(Integer)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
#     time_updated = Column(DateTime(timezone=True), onupdate=func.current_timestamp())