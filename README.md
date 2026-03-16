# hf-pipeline-practice

# 💕 내 말투 연애 캐릭터 분류기 💕
> My Love Language Classifier

내가 쓴 문장을 분석해서 연애 스타일 캐릭터 유형을 분류해주는 시스템.

---

## 📌 주제 선정 이유
> "내가 쓴 문장 하나로 나의 연애 스타일을 알 수 있다!

일상적인 연애 표현 문장을 입력하면 6가지 연애 캐릭터 유형 중 가장 가까운 유형을 분류해 줌

---

## Task & Models

### Task 
- `zero-shot-classification`
- 별도의 학습 데이터 없이 레이블 설명문만으로 분류

### Models (앙상블)
| 모델 | 파라미터 | 지원 언어 | 강점 |
|------|---------|-----------|------|
| [joeddav/xlm-roberta-large-xnli](https://huggingface.co/joeddav/xlm-roberta-large-xnli) | 560M | 15개 | 깊은 문맥 이해 |
| [MoritzLaurer/mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) | 280M | 100개 | 다국어 커버리지 |

---

## 🔧 앙상블 구조
```
입력 문장
    ↓
모델 A (xlm-roberta-large-xnli)   →   점수 A
모델 B (mDeBERTa-v3-base-mnli-xnli) → 점수 B
    ↓
두 모델 점수 평균 (앙상블)
    ↓
최종 유형 분류
```
두 모델의 분류 점수를 평균내어 최종 결과를 도출합니다.
단일 모델보다 안정적인 분류 결과를 제공합니다.


### 앙상블 적용 이유
단일 모델 사용 시 오분류 발견:
- "우리 천천히 알아가자" → ❌ 로맨티스트 (단일 모델)
- "우리 천천히 알아가자" → ✅ 신중파 (앙상블 적용 후)


---

## 💕 연애 캐릭터 유형 (6가지)

| 유형 | 설명 |
|------|------|
| 🎯 밀당고수 | 밀고 당기기를 반복하며 감정을 숨기는 타입 |
| 💝 순정파 | "너밖에 없어" 식의 헌신적 표현을 쓰는 타입 |
| 😇 유죄인간 | 무심한듯 의도치 않게 상대를 설레게 만드는 타입 |
| 🚀 직진형 | 좋아하는 감정을 망설임 없이 직접 표현하는 타입 |
| 🤔 신중파 | 감정 표현을 아끼고 천천히 관계를 발전시키는 타입 |
| 🌹 로맨티스트 | 감성적이고 낭만적인 표현을 즐기는 타입 |

---

## ⚠️ 한계 및 개선 방향

**현재 한계**
- 사용 모델이 NLI(자연어 추론) 기반으로 연애 도메인 특화 학습 데이터 없음
- 일부 문장에서 오분류 발생

**개선 방향**
- 연애 텍스트 데이터로 fine-tuning된 모델 적용
- 한국어 특화 감성 모델 검토

---

## 🚀 실행 방법

### 환경 설정
```bash
pip install -r requirements.txt
```

### 콘솔 버전
```bash
python console.py
```

### Streamlit 버전
```bash
streamlit run app.py
```

---


## 📁 파일 구조
```
├── app.py          # Streamlit UI
├── classifier.py   # 핵심 분류 로직 (앙상블)
├── console.py      # 콘솔 버전
├── requirements.txt
└── README.md
```