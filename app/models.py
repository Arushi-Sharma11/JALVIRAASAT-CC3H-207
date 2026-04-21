from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from app.database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String) # 'farmer' or 'general'
    fbs_score = Column(Float, default=500.0) # Starting Score
    savings_goal = Column(Float, default=0.0)
    last_month_spending = Column(Float, default=0.0)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    category = Column(String) # 'Essential', 'Productive', 'Waste'
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)