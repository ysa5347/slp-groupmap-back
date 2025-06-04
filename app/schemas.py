from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

"""
    example for schema layer
"""
class ShopBase(BaseModel):
    pk: int
    name: str
    dist: int
    walk_time: int
    pubtrans_time: int
    vehicle_time: int
    is_parking: int
    opening_info: Dict[str, Any]
    break_time: Optional[str] = None
    last_order: Optional[str] = None
    significant: str
    max_cap: int
    table_cap: int
    table_map_s3: str
    shop_map_s3: str
    naver_link: str
    kakao_link: str
    shop_type: int  # 모델과 일치하도록 수정
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
    shop_type: Optional[int] = None  # 카테고리 필터링 (1: 한식, 2: 중식, 3: 일식, 4: 양식, 5: 기타)
    min_capacity: Optional[int] = None  # 최소 인원수
    max_capacity: Optional[int] = None  # 최대 인원수
    tags: Optional[List[str]] = None  # 태그 필터링
    min_rating: Optional[float] = None
    is_active: Optional[bool] = True
    has_parking: Optional[bool] = None  # 주차 가능 여부

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

class ShopSort(BaseModel):
    sort_by: str = "name"  # 기본 정렬 필드
    order: SortOrder = SortOrder.asc  # asc 또는 desc

class ShopList(BaseModel):
    total: int
    shops: List[Shop]