from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from enum import Enum

from .database import Base

class TypeEnum(Enum):
    meal = "meal"
    drinks = "drinks"
    cafe = "cafe"

class Shop(Base):
    __tablename__ = "shops"

    pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    walk_dist = Column(Integer)
    vehicle_dist = Column(Integer)
    walk_time = Column(Integer)
    pubtrans_time = Column(Integer)
    vehicle_time = Column(Integer)
    is_parking = Column(Boolean)
    opening_hours = Column(JSON)
    max_cap = Column(Integer)
    table_cap = Column(Integer)
    table_map_S3 = Column(String(255))
    shop_map_S3 = Column(String(255))
    naver_link = Column(String(255))
    kakao_link = Column(String(255))
    type = Column(Enum(TypeEnum), nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    tags = relationship("Tag", backref="shops")

class Tag(Base):
    __tablename__ = "tags"

    pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    description = Column(Text)

    def __repr__(self):
        return f"{self.name}"