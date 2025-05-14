import os
import pandas as pd
from dotenv import load_dotenv
from collections import OrderedDict
from app.database import SessionLocal
from app.models.shop import Shop
from app.models.tag import Tag
from app.constants import DAYS, SHOP_TYPE_MAP

load_dotenv()
EXCEL_PATH = os.getenv("EXCEL_PATH")

def parse_opening_hours(row):
    return {
        day: row[day] if not pd.isna(row[day]) and row[day] != "X" else None
        for day in DAYS
    }

def parse_tags(tag_string):
    if pd.isna(tag_string):
        return []
    return [tag.strip() for tag in tag_string.split(',') if tag.strip()]

def insert_data():
    db = SessionLocal()

    try:
        df = pd.read_excel(EXCEL_PATH, header=1)

        for _, row in df.iterrows():
            name = row[1]
            dist = int(row[2]) if not pd.isna(row[2]) else None
            walk_time = int(row[3]) if not pd.isna(row[3]) else None
            vehicle_time = int(row[4]) if not pd.isna(row[4]) else None
            is_parking = int(row[5]) if not pd.isna(row[5]) else None

            opening_hours = parse_opening_hours(row)
            break_time = row[13] if not pd.isna(row[13]) else None
            last_order = row[14] if not pd.isna(row[14]) else None
            significant = row[15] if not pd.isna(row[15]) else None

            max_cap = int(row[16]) if not pd.isna(row[16]) else None
            table_cap = int(row[17]) if not pd.isna(row[17]) else None
            naver_link = row[18]
            kakao_link = row[19]

            shop_type_index = row[20]
            shop_type = SHOP_TYPE_MAP.get(shop_type_index, 0) # default = 'meal'

            tag_names = parse_tags(row[21])

            shop = Shop(
                name=name,
                dist=dist,
                walk_time=walk_time,
                vehicle_time=vehicle_time,
                is_parking=is_parking,
                opening_hours=opening_hours,
                break_time=break_time,
                last_order=last_order,
                significant=significant,
                max_cap=max_cap,
                table_cap=table_cap,
                naver_link=naver_link,
                kakao_link=kakao_link,
                shop_type=shop_type,
                table_map_s3=None,
                shop_map_s3=None,
                is_active=False,
                is_deleted=True,
                created_at=None,
                updated_at=None
            )

            for tag_name in tag_names:
                tag = db.query(Tag).filter_by(tag_name=tag_name).first()
                if not tag:
                    tag = Tag(tag_name=tag_name)
                    db.add(tag)
                shop.tags.append(tag)

            db.add(shop)

        db.commit()
        print("EXCEL data are inserted in db.")

    except Exception as e:
        db.rollback()
        print("DB ERROR: ", e)

    finally:
        db.close()

if __name__ == '__main__':
    insert_data()

