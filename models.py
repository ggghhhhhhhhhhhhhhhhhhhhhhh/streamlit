# models.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_admin = Column(Boolean, default=False)

class LostItem(Base):
    __tablename__ = 'lost_items'
    id = Column(Integer, primary_key=True)
    owner_name = Column(String(100))
    item_desc = Column(String(200))
    last_seen_location = Column(String(100))
    image_url = Column(String(200), nullable=True)
    status = Column(String(20), default='Lost')
    user_id = Column(Integer, ForeignKey('users.id'))

class FoundItem(Base):
    __tablename__ = 'found_items'
    id = Column(Integer, primary_key=True)
    finder_name = Column(String(100))
    contact_info = Column(String(100))
    item_desc = Column(String(200))
    found_location = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
