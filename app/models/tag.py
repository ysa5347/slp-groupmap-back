from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .association import shop_tags
from .base import Base

class Tag(Base):
    __tablename__ = "tags"

    pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tag_name = Column(String(255), index=True, nullable=False)
    description = Column(Text)

    shops = relationship("Shop", secondary=shop_tags, back_populates="tags")

    def __repr__(self):
        return f"{self.tag_name}"