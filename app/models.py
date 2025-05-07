from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.types import Enum as SQLEnum
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Table

from .database import Base

shop_type_enum = SQLEnum('cafe', 'meal', 'drink', name='shop_type_enum', create_type=False)

shop_tags = Table(
    'shop_tags',
    Base.metadata,
    Column('shop_id', Integer, ForeignKey('shop_details.pk'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.pk'), primary_key=True)
)

class Shop(Base):
    __tablename__ = "shop_details"

    pk = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    walk_dist = Column(Integer)
    vehicle_dist = Column(Integer)
    walk_time = Column(Integer)
    pubtrans_time = Column(Integer)
    vehicle_time = Column(Integer)
    is_parking = Column(Boolean)
    opening_hours = Column(JSONB)
    max_cap = Column(Integer)
    table_cap = Column(Integer)
    table_map_s3 = Column(String)
    shop_map_s3 = Column(String)
    naver_link = Column(String)
    kakao_link = Column(String)
    shop_type = Column(shop_type_enum, nullable=False)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    tags = relationship("Tag", secondary=shop_tags, back_populates="shops")

class Tag(Base):
    __tablename__ = "tags"

    pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    description = Column(Text)

    shops = relationship("Shop", secondary=shop_tags, back_populates="tags" )
    def __repr__(self):
        return f"{self.name}"
