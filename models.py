from sqlalchemy import Column, Integer, String, Text, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# Initialize database connection
DATABASE_URL = "sqlite:///instance/recoverease.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

class LostItem(Base):
    __tablename__ = 'lost_items'
    id = Column(Integer, primary_key=True)
    owner_name = Column(String(100), nullable=False)
    item_desc = Column(Text, nullable=False)
    last_seen_location = Column(String(100), nullable=False)
    image_url = Column(String(200))
    status = Column(String(20), default='Lost')

class FoundItem(Base):
    __tablename__ = 'found_items'
    id = Column(Integer, primary_key=True)
    finder_name = Column(String(100), nullable=False)
    contact_info = Column(String(100), nullable=False)
    item_desc = Column(Text, nullable=False)


