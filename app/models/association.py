from sqlalchemy import Column, Integer, Table, ForeignKey
from .base import Base

shop_tags = Table(
    'shop_tags',
    Base.metadata,
    Column('shop_id', Integer, ForeignKey('shop_details.pk'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.pk'), primary_key=True)
)