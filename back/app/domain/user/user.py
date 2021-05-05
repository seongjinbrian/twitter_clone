from sqlalchemy import Column, String, Integer
from app.domain import Base

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id: int = Column(Integer, primary_key = True) 
    username: str = Column(String(24), nullable=False)
    email: str = Column(String(64), nullable=False)
    password: str = Column(String(64), nullable=False)