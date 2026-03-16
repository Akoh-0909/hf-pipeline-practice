# hf-pipeline-practice

# 내 말투 연애 캐릭터 분류기 💕

내가 쓴 문장을 분석해서 연애 스타일 캐릭터 유형을 분류해주는 시스템입니다.

## Task
- sentence-similarity

## Model
- [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask)

## 연애 캐릭터 유형
| 유형 | 설명 |
|------|------|
| 🎯 밀당고수 | 밀고 당기기를 반복하며 감정을 숨기는 타입 |
| 💝 순정파 | 감정을 솔직하고 진지하게 표현하는 타입 |
| 😇 유죄인간 | 무심한 행동으로 의도치 않게 상대를 설레게 만드는 타입 |
| 🚀 직진형 | 좋아하는 감정을 망설임 없이 직접 표현하는 타입 |
| 🤔 신중파 | 감정 표현을 아끼고 천천히 관계를 발전시키는 타입 |
| 🌹 로맨티스트 | 감성적이고 낭만적인 표현을 즐기는 타입 |

## 실행 방법

### 콘솔
```bash
python console.py
```

### Streamlit
```bash
streamlit run app.py
```

## 파일 구조
```
├── app.py          # Streamlit UI
├── classifier.py   # 핵심 분류 로직
├── console.py      # 콘솔 버전
├── requirements.txt
└── README.md
```