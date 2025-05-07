import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models, routers
from .database import engine

# 데이터베이스 테이블 생성 (존재하는 DB 유지)
#models.Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="group- API",
    description="밥술카 가게 정보를 검색하고 조회하는 API",
    version="0.1.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(routers.router)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
