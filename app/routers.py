from fastapi import APIRouter, Depends, Query
from typing import Optional

from . import controllers, schemas
from .database import get_db

router = APIRouter(prefix="/shops", tags=["shops"])

@router.get("/", response_model=schemas.ShopList)
def read_shops(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    min_rating: Optional[float] = None,
    is_active: Optional[bool] = True,
    sort_by: Optional[str] = "name",
    order: Optional[str] = "asc"
):
    return controllers.ShopController.get_shops(
        skip=skip,
        limit=limit,
        category=category,
        min_rating=min_rating,
        is_active=is_active,
        sort_by=sort_by,
        order=order
    )

@router.get("/{shop_id}", response_model=schemas.Shop)
def read_shop(shop_id: int):
    return controllers.ShopController.get_shop(shop_id=shop_id)