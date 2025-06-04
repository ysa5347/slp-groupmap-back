from typing import Optional, List, Dict, Any
from pydantic import BaseModel, validator
from datetime import datetime
from enum import Enum

"""
    example for schema layer
"""
class ShopBase(BaseModel):
    pk: int
    name: str

    dist: Optional[int] = None
    walk_time: Optional[int] = None
    pubtrans_time: Optional[int] = None
    vehicle_time: Optional[int] = None
    is_parking: Optional[int] = None
    opening_info: Optional[Dict[str, Any]] = None
    significant: Optional[str] = None
    max_cap: Optional[int] = None
    table_cap: Optional[int] = None
    table_map_s3: Optional[str] = None
    shop_map_s3: Optional[str] = None
    naver_link: Optional[str] = None
    kakao_link: Optional[str] = None
    type: Optional[int] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: List[str] = []  # List of tag names associated with the shop

    # tags필드 처리
    @validator('tags', pre=True)
    def extract_tag(cls, v: Any):
        if isinstance(v, list):
            return [tag.name if hasattr(tag, "name") else str(tag) for tag in v]
        return v

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
    sort_by: Optional[str] = "walk_dist"  # 기본 정렬 필드
    order: Optional[SortOrder] = SortOrder.asc  # asc 또는 desc

class ShopList(BaseModel):
    total: int
    shops: List[Shop]