## careerfit_AI_new
2026년 여름 계절학기(데이원 컴퍼니)

# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

## 프로젝트 개요

사용자의 전공, 역량, 희망 직종을 입력받아 적절한 취업 공고를 추천하는 언어 모델 서버를 구축하였다.

## 기술 스택

| 영역 | 기술 |
|---|---|
| 백엔드 | Python, FastAPI |
| AI API | Gemini 2.5 Flash-Lite |
| 데이터 | Pandas, SQLite, ChromaDB |
| 프론트엔드 | React, Vite |
| 실행 환경 | Docker |

## 진행 현황



- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

* CareerFit AI 서비스의 문제 정의 및 목표 설정
* AI 서비스 기획 캔버스(Project Plan) 작성
* GitHub Repository 생성 및 프로젝트 구조 설계
* Python 개발 환경 및 Cursor 설정
* AI 조교 규칙(AI_TA_RULES), 프롬프트(PROMPTS), 체크리스트(CHECKLIST) 등 프로젝트 문서 작성

> 1일차 결과: 프로젝트의 개발 방향과 AI 응답 규칙을 문서화하고 협업 기반을 마련하였다.

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결

* Python 가상환경 및 프로젝트 실행 환경 세팅 완료
* FastAPI 기반 `/health`, `/jobs`, `/analyze` 엔드포인트 구현
* Gemini 2.5 Flash-Lite API 연동 및 응답 확인
* 개발·테스트를 위한 `MOCK_MODE` 환경변수 구성
* API 구조와 AI 응답 흐름의 기본 하네스 구축 완료

> 2일차 결과: 사용자 입력을 받아 AI 분석 결과를 반환하는 기본 백엔드 구조를 완성하였다.

- [x] 3일차: 데이터 파이프라인 구축

* 취업 공고 CSV(`job.csv`) 데이터 전처리(Pandas)
* 결측치 제거 및 스킬 표준화
* SQLite에 구조화 데이터 저장
* RAG용 문서 생성
* ChromaDB에 벡터 데이터 저장
* 의미 기반 검색(Search) 테스트

> 3일차 결과: 정형 데이터(SQLite)와 의미 기반 검색(ChromaDB)을 함께 활용하는 데이터 파이프라인을 구축하였다.

- [x] 4일차: RAG 기반 서비스 + React UI

* ChromaDB 검색 결과와 언어 모형 Gemini를 연결하여 RAG 구현
* `/analyze` API에서 근거 기반 응답 생성
* `sources`와 `confidence`를 포함한 구조화된 JSON 응답 구현
* React UI와 FastAPI 연동
* `ResultCard` 및 `SourceCard` 구현
* RAG 평가 및 LLM Instructions 개선

> 4일차 결과: 사용자의 역량과 가장 유사한 취업 공고를 검색하여 근거 기반 분석 결과를 제공하는 AI 서비스를 완성하였다.

- [x] 5일차: Docker + 포트폴리오 완성
* `Dockerfile` 작성 및 컨테이너 실행
* `.dockerignore`를 활용한 보안 설정
* `README` 및 프로젝트 문서 최종 정리
* GitHub Repository 최종 검토
* 발표 자료 및 포트폴리오 준비

> 5일차 결과: 