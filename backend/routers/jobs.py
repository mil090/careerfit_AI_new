from fastapi import APIRouter

from typing import List

router = APIRouter()



# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다

MOCK_JOBS = [

    {
        "id": 1,
        "company": "K리그 데이터센터",
        "title": "스포츠 데이터 분석가",
        "required_skills": ["Python", "SQL", "통계"],
        "preferred_skills": ["Tableau", "Pandas"],
        "description": "경기 및 선수 데이터를 분석하여 팀 전력 강화 의사결정을 지원합니다. 경기 지표 리포트 작성과 데이터 기반 인사이트 도출 업무를 수행합니다.",
        "deadline": "2026-08-31"
    },

    {
        "id": 2,
        "company": "SPOTV",
        "title": "스포츠 AI 분석 인턴",
        "required_skills": ["Python", "데이터 분석", "시각화"],
        "preferred_skills": ["SQL", "머신러닝"],
        "description": "경기 기록과 이벤트 데이터를 분석하여 시청자용 분석 콘텐츠 제작을 지원합니다. 데이터 정제와 리포트 자동화 업무를 함께 수행합니다.",
        "deadline": "2026-08-31"
    },

    {
        "id": 3,
        "company": "LG 스포츠",
        "title": "전력분석 데이터 연구원",
        "required_skills": ["Python", "SQL", "머신러닝"],
        "preferred_skills": ["PyTorch", "통계"],
        "description": "선수 성과 및 경기 전략 데이터를 분석하여 전력 강화 방향을 제안합니다. 분석 결과를 시각화하고 내부 의사결정을 지원합니다.",
        "deadline": "2026-08-31"
    }

]



@router.get("/jobs", tags=["Jobs"])

def get_jobs():

    """

    취업 공고 목록을 반환하는 엔드포인트.

    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.

    """

    return {

        "count": len(MOCK_JOBS),

        "jobs": MOCK_JOBS

    }



@router.get("/jobs/{job_id}", tags=["Jobs"])

def get_job_by_id(job_id: int):

    """

    특정 공고의 상세 정보를 반환한다.

    """

    for job in MOCK_JOBS:

        if job["id"] == job_id:

            return job

    # 찾지 못한 경우

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")