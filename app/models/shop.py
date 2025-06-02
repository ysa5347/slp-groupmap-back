from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .association import shop_tags
from .base import Base

class Shop(Base):
    __tablename__ = "shop_details"

    pk = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(127), index=True, nullable=False)
    dist = Column(Integer)
    walk_time = Column(Integer)
    pubtrans_time = Column(Integer)
    vehicle_time = Column(Integer)
    is_parking = Column(Integer)
    opening_hours = Column(JSON)
    break_time = Column(String(255))
    last_order = Column(String(255))
    significant = Column(String(255))
    max_cap = Column(Integer)
    table_cap = Column(Integer)
    table_map_s3 = Column(String(255))
    shop_map_s3 = Column(String(255))
    naver_link = Column(String(255))
    kakao_link = Column(String(255))
    shop_type = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    tags = relationship("Tag", secondary=shop_tags, back_populates="shops")