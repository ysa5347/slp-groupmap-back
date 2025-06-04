from fastapi import APIRouter, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session

from . import controllers, schemas
from .database import get_db

router = APIRouter(prefix="/shops", tags=["shops"])

@router.get("/", response_model=schemas.ShopList)
def read_shops(
    skip: int = 0,
    limit: int = 100,
    shop_type: Optional[int] = Query(None, description="카테고리 필터 (0: 밥, 1: 카, 2: 술)"),
    min_capacity: Optional[int] = Query(None, description="최소 인원수"),
    max_capacity: Optional[int] = Query(None, description="최대 인원수"),
    tags: Optional[str] = Query(None, description="태그 필터 (쉼표로 구분)"),
    min_rating: Optional[float] = Query(None, description="최소 평점"),
    is_active: Optional[bool] = Query(True, description="활성 상태"),
    has_parking: Optional[bool] = Query(None, description="주차 가능 여부"),
    sort_by: Optional[str] = Query("name", description="정렬 기준 필드"),
    order: Optional[str] = Query("asc", description="정렬 순서 (asc/desc)"),
    db: Session = Depends(get_db)
):
    # 태그 문자열을 리스트로 변환
    tag_list = None
    if tags:
        tag_list = [tag.strip() for tag in tags.split(",") if tag.strip()]
    
    return controllers.ShopController.get_shops(
        db=db,
        skip=skip,
        limit=limit,
        shop_type=shop_type,
        min_capacity=min_capacity,
        max_capacity=max_capacity,
        tags=tag_list,
        min_rating=min_rating,
        is_active=is_active,
        has_parking=has_parking,
        sort_by=sort_by,
        order=order
    )

@router.get("/{shop_id}", response_model=schemas.Shop)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    return controllers.ShopController.get_shop(db, shop_id=shop_id)