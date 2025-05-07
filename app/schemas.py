from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

"""
    example for schema layer
"""
class ShopBase(BaseModel):
    pk: int
    name: str
    walk_dist: int
    vehicle_dist: int
    walk_time: int
    pubtrans_time: int
    vehicle_time: int
    is_parking: bool
    opening_hours: dict
    max_cap: int
    table_cap: int
    table_map_S3: str
    shop_map_S3: str
    naver_link: str
    kakao_link: str
    type: str
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime
    tags: List[str] = []  # List of tag names associated with the shop

class ShopCreate(ShopBase):
    pass

class ShopUpdate(ShopBase):
    pass

class Shop(ShopBase):
    pass

class ShopFilter(BaseModel):
    pass

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class ShopSort(BaseModel):
    sort_by: str = "name"  # 기본 정렬 필드
    order: SortOrder = SortOrder.asc  # asc 또는 desc

class ShopList(BaseModel):
    total: int
    shops: List[Shop]