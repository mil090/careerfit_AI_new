# harness/skills/design-skill.md — CareerFit AI UI 디자인 규칙



## 컬러 팔레트

- primary: #3B82F6 (파란색 — 신뢰, 전문성)

- secondary: #10B981 (초록색 — 성장, 추천)

- background: #F8FAFC (연한 회색)

- text-primary: #1E293B

- text-muted: #64748B

- border: #E2E8F0

- error: #EF4444



## 타이포그래피

- 제목: text-2xl font-bold text-slate-800

- 소제목: text-lg font-semibold text-slate-700

- 본문: text-base text-slate-600

- 설명: text-sm text-slate-500



## 컴포넌트 구조

- App.jsx: 최상위, 상태 관리, API 요청

- InputForm.jsx: 전공·스킬·직무 입력 폼

- ResultCard.jsx: AI 분석 답변 출력 (초록 왼쪽 테두리)

- SourceCard.jsx: 출처 공고 목록 출력



## 레이아웃 규칙

- 최대 너비: max-w-2xl mx-auto

- 카드 내부 여백: p-6

- 컴포넌트 간격: gap-4 / space-y-4

- 모서리: rounded-xl (카드), rounded-lg (버튼)



## 금지 사항

- API Key를 화면에 표시하거나 localStorage에 저장

- 다크 배경에 흰 텍스트 (가독성 우선)

- 아이콘 없이 버튼만 사용 (텍스트 레이블 필수)



