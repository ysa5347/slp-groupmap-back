from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc, asc, and_, or_

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
        query = db.query(models.Shop).options(joinedload(models.Shop.tags))
        
        # 필터 적용
        if filters:
            # 카테고리(shop_type) 필터링
            if filters.shop_type is not None:
                query = query.filter(models.Shop.shop_type == filters.shop_type)
            
            # 인원수 필터링
            if filters.min_capacity is not None:
                query = query.filter(models.Shop.max_cap >= filters.min_capacity)
            if filters.max_capacity is not None:
                query = query.filter(models.Shop.max_cap <= filters.max_capacity)
            
            # 태그 필터링
            if filters.tags and len(filters.tags) > 0:
                # 지정된 태그 중 하나라도 포함된 상점 찾기
                tag_conditions = []
                for tag_name in filters.tags:
                    tag_conditions.append(models.Shop.tags.any(models.Tag.tag_name.ilike(f"%{tag_name}%")))
                query = query.filter(or_(*tag_conditions))
            
            # 최소 평점 필터링 (나중에 평점 필드가 추가되면 사용)
            # if filters.min_rating is not None:
            #     query = query.filter(models.Shop.rating >= filters.min_rating)
            
            # 활성 상태 필터링
            if filters.is_active is not None:
                query = query.filter(models.Shop.is_active == filters.is_active)
            
            # 주차 가능 여부 필터링
            if filters.has_parking is not None:
                if filters.has_parking:
                    query = query.filter(models.Shop.is_parking == 1)
                else:
                    query = query.filter(models.Shop.is_parking == 0)
        
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
        
        # 태그 이름 추출
        for shop in shops:
            shop.tags = [tag.tag_name for tag in shop.tags]
        
        return {
            "total": total,
            "shops": shops
        }
    
    @staticmethod
    def get_shop(db: Session, shop_id: int):
        return db.query(models.Shop).filter(models.Shop.pk == shop_id).first()