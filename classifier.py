from transformers import pipeline

# HuggingFace Pipeline 로드
# zero-shot-classification + 다국어 모델 (한국어 지원)
classifier = pipeline(
    'zero-shot-classification',
    model='joeddav/xlm-roberta-large-xnli'
)

# 연애 캐릭터 유형 정의
# key: UI 표시용 이름 / value: 모델이 이해할 설명문
labels = {
    "🎯 밀당고수(The Master of Push-and-Pull)":     "a person who uses ambiguous expressions and irregular response times. Strategically conceals true feelings to maintain mystery and control the pace of the relationship. Prefers indirect flirting over direct confessions.",
    "💝 순정파(The Devoted Soul)":      "a person who demonstrates high emotional commitment and consistency. Uses sincere, unadorned language and shows deep empathy. Focuses on building a long-term, stable bond through honest communication and vulnerability.",
    "😇 유죄인간(The Accidental Heartthrob)":    "a person who naturally kind and charming without realizing the romantic impact on others. Uses polite and caring language toward everyone, often leading to unintentional fluttering of hearts or misunderstandings.",
    "🚀 직진형(The Bold Go-Getter)":      "a person who expresses romantic interest directly and immediately. Values transparency and takes the initiative in asking for dates or confessing feelings. Minimal use of metaphors; highly action-oriented and straightforward.",
    "🤔 신중파(The Cautious Observer)":      "a person who suggests slowing down and taking time to get to know each other better before committing. Prefers gradual relationship progression and avoids rushing into romance.",
    "🌹 로맨티스트(The Hopeless Romantic)":  "a person who enjoys poetic and sentimental expressions in daily conversation. Focuses on creating romantic narratives, emotional resonance, and special atmospheres. Values 'the little things' and idealistic romantic gestures."
}

def classify(text: str) -> list:
    """
    입력 텍스트를 연애 캐릭터 유형으로 분류합니다.
    반환값: [(유형이름, 점수), ...] 높은 점수 순 정렬
    """
    # 모델용 설명문 리스트
    candidate_labels = list(labels.values())

    # pipeline 실행
    result = classifier(text, candidate_labels)

    # 설명문 → UI 표시 이름으로 변환
    desc_to_name = {v: k for k, v in labels.items()}
    output = [
        (desc_to_name[label], round(score, 4))
        for label, score in zip(result['labels'], result['scores'])
    ]

    return output