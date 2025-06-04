from typing import List, Optional
from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session

from . import schemas, services
from .database import get_db

"""
    example for controller layer
    - FastAPI의 라우터와 서비스 레이어를 연결하는 역할을 합니다.
    - HTTP 요청을 처리하고, 서비스 레이어를 호출하여 결과를 반환합니다.
    - 요청 유효성 검사 및 예외 처리를 수행합니다.
"""

class ShopController:
    @staticmethod
    def get_shops(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
        category: Optional[str] = None,
        min_rating: Optional[float] = None,
        is_active: Optional[bool] = True,
        sort_by: Optional[str] = "name",
        order: Optional[str] = "asc"
    ):
        # 필터와 정렬 객체 생성
        filters = schemas.ShopFilter(
            category=category,
            min_rating=min_rating,
            is_active=is_active
        )
        
        sort = schemas.ShopSort(
            sort_by=sort_by,
            order=order
        )
        
        # 서비스 호출
        result = services.ShopService.get_shops(
            db=db, 
            skip=skip, 
            limit=limit, 
            filters=filters,
            sort=sort
        )
        
        return schemas.ShopList(
            total=result["total"],
            shops=result["shops"]
        )
    
    @staticmethod
    def get_shop(db: Session, shop_id: int):
        shop = services.ShopService.get_shop(db, shop_id=shop_id)
        if shop is None:
            raise HTTPException(status_code=404, detail="가게를 찾을 수 없습니다")
        return shop