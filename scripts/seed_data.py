from app.database import SessionLocal
from app.models import Shop, Tag, shop_type_enum

# DB 세션 생성
db = SessionLocal()

# 예시 태그 생성
tag1 = Tag(name="브런치", description="브런치 전문점")
tag2 = Tag(name="데이트", description="연인과 방문하기 좋은 장소")
tag3 = Tag(name="단체석", description="단체 손님 수용 가능")
tag4 = Tag(name="조용한", description="조용한 분위기의 카페")
tag5 = Tag(name="야외", description="야외 좌석이 있는 매장")

tags = [tag1, tag2, tag3, tag4, tag5]
db.add_all(tags)
db.commit()

# 예시 매장 생성
shop_examples = [
    Shop(
        name="CAFE 1",
        walk_dist=300,
        vehicle_dist=1200,
        walk_time=5,
        pubtrans_time=10,
        vehicle_time=3,
        is_parking=True,
        opening_hours={"mon-fri": "09:00-20:00", "sat-sun": "10:00-22:00"},
        max_cap=50,
        table_cap=20,
        table_map_s3="s3://example-bucket/table_map1.png",
        shop_map_s3="s3://example-bucket/shop_map1.png",
        naver_link="https://naver.me/abc123",
        kakao_link="https://kakao.link/xyz123",
        shop_type='cafe',
        is_active=True,
        is_deleted=False,
        tags=[tag4, tag5]
    ),
    Shop(
        name="MEAL 1",
        walk_dist=1000,
        vehicle_dist=2000,
        walk_time=15,
        pubtrans_time=25,
        vehicle_time=7,
        is_parking=True,
        opening_hours={"daily": "11:00-23:00"},
        max_cap=120,
        table_cap=40,
        table_map_s3="s3://example-bucket/table_map2.png",
        shop_map_s3="s3://example-bucket/shop_map2.png",
        naver_link="https://naver.me/grill456",
        kakao_link="https://kakao.link/grill456",
        shop_type='meal',
        is_active=True,
        is_deleted=False,
        tags=[tag1, tag3]
    ),
    Shop(
        name="CAFE 2",
        walk_dist=200,
        vehicle_dist=800,
        walk_time=3,
        pubtrans_time=8,
        vehicle_time=2,
        is_parking=False,
        opening_hours={"mon-fri": "10:00-21:00"},
        max_cap=30,
        table_cap=15,
        table_map_s3="s3://example-bucket/table_map3.png",
        shop_map_s3="s3://example-bucket/shop_map3.png",
        naver_link="https://naver.me/walk789",
        kakao_link="https://kakao.link/walk789",
        shop_type='cafe',
        is_active=True,
        is_deleted=False,
        tags=[tag2, tag4]
    ),
    Shop(
        name="MEAL 1",
        walk_dist=700,
        vehicle_dist=1800,
        walk_time=10,
        pubtrans_time=15,
        vehicle_time=5,
        is_parking=False,
        opening_hours={"fri-sun": "17:00-01:00"},
        max_cap=100,
        table_cap=35,
        table_map_s3="s3://example-bucket/table_map4.png",
        shop_map_s3="s3://example-bucket/shop_map4.png",
        naver_link="https://naver.me/night123",
        kakao_link="https://kakao.link/night123",
        shop_type='meal',
        is_active=True,
        is_deleted=False,
        tags=[tag5, tag3]
    ),
    Shop(
        name="DRINK 1",
        walk_dist=400,
        vehicle_dist=1000,
        walk_time=6,
        pubtrans_time=12,
        vehicle_time=4,
        is_parking=False,
        opening_hours={"mon-sat": "18:00-02:00"},
        max_cap=80,
        table_cap=30,
        table_map_s3="s3://example-bucket/table_map5.png",
        shop_map_s3="s3://example-bucket/shop_map5.png",
        naver_link="https://naver.me/drink321",
        kakao_link="https://kakao.link/drink321",
        shop_type='drink',
        is_active=True,
        is_deleted=False,
        tags=[tag2, tag1]
    ),
]

db.add_all(shop_examples)
db.commit()
db.close()

print("Seed data inserted successfully.")
