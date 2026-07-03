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



# 실행 테스트

if __name__ == "__main__":

 df_jobs = load_data(JOBS_CSV)

 print()

 print("=== 처음 3행 미리보기 ===")

 print(df_jobs.head(3).to_string())

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