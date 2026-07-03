import pandas as pd

import sqlite3

import json

import os



# ─── 1. 파일 경로 설정 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JOBS_CSV = os.path.join(BASE_DIR, "jobs.csv")

DB_PATH = os.path.join(BASE_DIR, "careerfit.db")

RAG_JSON = os.path.join(BASE_DIR, "rag_documents.json")



# ─── 2. CSV 읽기 

def load_data(filepath: str) -> pd.DataFrame:

    """

    CSV 파일을 읽어 DataFrame으로 반환합니다.

    인코딩 오류가 발생하면 cp949로 재시도합니다.

    """

    try:

        df = pd.read_csv(filepath, encoding="utf-8")

        print(f"✅ 파일 읽기 성공 (UTF-8): {filepath}")

    except UnicodeDecodeError:

        df = pd.read_csv(filepath, encoding="cp949")

        print(f"✅ 파일 읽기 성공 (CP949): {filepath}")

    print(f"   행 수: {len(df)}, 열 수: {len(df.columns)}")

    print(f"   컬럼: {df.columns.tolist()}")

    return df

# 결측치 확인 함수 추가

def check_missing(df: pd.DataFrame) -> pd.DataFrame:

    """

    각 컬럼의 결측치(빈값) 수와 비율을 확인합니다.

    요리 비유: 재료 중 빠진 것이 있는지 확인하는 단계입니다.

    """

    print("\n=== 결측치 확인 ===")

    missing = df.isnull().sum()

    missing_pct = (df.isnull().sum() / len(df) * 100).round(1)

    result = pd.DataFrame({

        "결측치 수": missing,

        "결측치 비율(%)": missing_pct

    })

    print(result[result["결측치 수"] > 0])  # 결측치 있는 컬럼만 출력

    if missing.sum() == 0:

        print("   ✅ 결측치 없음")

    else:

        print(f"   ⚠️  총 {missing.sum()}개 결측치 발견")

    return df

# 결측치 처리 함수 추가

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    결측치를 처리합니다.
    - 텍스트 컬럼: 빈 문자열로 채웁니다
    - 핵심 컬럼이 비어있는 행은 제거합니다
    """
    print("\n=== 결측치 처리 ===")
    before = len(df)

    # 핵심 컬럼(title, required_skills)이 비어있는 행 제거
    # 이 정보가 없으면 RAG 검색에 의미가 없기 때문입니다
    df = df.dropna(subset=["title", "required_skills"])

    # 나머지 텍스트 컬럼은 빈 문자열로 채웁니다
    text_cols = ["preferred_skills", "description", "company", "job_type"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("")

    after = len(df)
    print(f"   처리 전: {before}행 → 처리 후: {after}행")
    print(f"   제거된 행: {before - after}행")
    return df

# 중복 확인 및 제거 함수 추가

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:

    """

    중복 행을 확인하고 제거합니다.

    company + title 조합이 같으면 중복으로 판단합니다.

    """

    print("\n=== 중복 확인 ===")

    before = len(df)

    # company + title 기준으로 중복 확인

    duplicated = df.duplicated(subset=["company", "title"], keep=False)

    if duplicated.sum() > 0:

        print(f"   ⚠️  중복 발견: {duplicated.sum()}행")

        print(df[duplicated][["company", "title"]])

    else:

        print("   ✅ 중복 없음")

    # 첫 번째 행만 남기고 중복 제거

    df = df.drop_duplicates(subset=["company", "title"], keep="first")

    after = len(df)

    print(f"   제거 후: {after}행 (제거: {before - after}행)")

    return df

# 실행 테스트

if __name__ == "__main__":

    # 1. 읽기

    df_jobs = load_data(JOBS_CSV)

    # 2. 결측치 확인

    df_jobs = check_missing(df_jobs)

    # 3. 결측치 처리

    df_jobs = handle_missing(df_jobs)

    # 4. 중복 제거

    df_jobs = remove_duplicates(df_jobs)

    print(f"\n✅ 전처리 완료: 최종 {len(df_jobs)}행")