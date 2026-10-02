from sqlalchemy import Column, String, Integer, Numeric, Boolean, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Meals(Base):
    __tablename__ = "meals"
    __table_args__ = {"schema": "food_service"}  # Maps directly to DBeaver food schema

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(String(100), nullable=False)
    calories = Column(Integer, nullable=False)
    protein_grams = Column(Numeric(10, 2), nullable=False)
    carbs_grams = Column(Numeric(10, 2), nullable=False)
    fat_grams = Column(Numeric(10, 2), nullable=False)
    serving_size = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth_service"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

class user_macro_targets(Base):
    __tablename__ = "user_macro_targets"
    __table_args__ = {"schema": "nutrition_service"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), nullable=False)  # Loosely coupled data reference
    target_calories = Column(Integer, nullable=False)
    target_protein_grams = Column(Numeric(10, 2), nullable=False)
    target_carbs_grams = Column(Numeric(10, 2), nullable=False)
    target_fat_grams = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

class food_logs(Base):
    __tablename__ = "food_logs"
    __table_args__ = {"schema": "nutrition_service"}

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    user_id = Column(UUID(as_uuid=True), nullable=False)  # Loosely coupled data reference
    meal_id = Column(UUID(as_uuid=True), nullable=False)  # Loosely coupled data reference
    log_date = Column(DateTime, nullable=False)
    quantity_served = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))