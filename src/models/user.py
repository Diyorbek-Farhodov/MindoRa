from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

from src.base.pg_db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    profile_image = Column(String, nullable=True)
    is_active = Column(Boolean, default=False, comment="Faol holat")
    is_admin = Column(Boolean, default=False, comment="Admin huquqi")
    created_at = Column(DateTime, default=datetime.utcnow, comment="Yaratilgan vaqt")
