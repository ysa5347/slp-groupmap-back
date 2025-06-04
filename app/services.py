from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc

from . import models, schemas

"""
example for service layer
"""

class ShopService:
    @staticmethod
    def get_shops(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        filters: Optional[schemas.ShopFilter] = None,
        sort: Optional[schemas.ShopSort] = None
    ) -> Dict[str, Any]:
        query = db.query(models.Shop)
        
        # 필터 적용
        if filters:
            if filters.category:
                query = query.filter(models.Shop.category == filters.category)
            if filters.min_rating is not None:
                query = query.filter(models.Shop.rating >= filters.min_rating)
            if filters.is_active is not None:
                query = query.filter(models.Shop.is_active == filters.is_active)
        
        # 정렬 적용
        if sort:
            sort_column = getattr(models.Shop, sort.sort_by, models.Shop.name)
            if sort.order.lower() == "desc":
                query = query.order_by(desc(sort_column))
            else:
                query = query.order_by(asc(sort_column))
        
        # 전체 결과 수 계산
        total = query.count()
        
        # 페이지네이션 적용
        shops = query.offset(skip).limit(limit).all()
        
        return {
            "total": total,
            "shops": shops
        }
    
    @staticmethod
    def get_shop(db: Session, shop_id: int):
        return db.query(models.Shop).filter(models.Shop.pk == shop_id).first()