from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.domain import Base

class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("users.id"))
    user = relationship('Users', foreign_keys=uid)
    title = Column(String(256))
    content = Column(String(2048))