from transformers import pipeline

# HuggingFace Pipeline 로드

# 모델 A
classifier_a = pipeline(
    'zero-shot-classification',
    model='joeddav/xlm-roberta-large-xnli'
)

# 모델 B
classifier_b = pipeline(
    'zero-shot-classification',
    model='MoritzLaurer/mDeBERTa-v3-base-mnli-xnli'
)

# 연애 캐릭터 유형 정의

labels = {
    "🎯 밀당고수(The Master of Push-and-Pull)":     "a person who uses ambiguous expressions and irregular response times. Strategically conceals true feelings to maintain mystery and control the pace of the relationship. Prefers indirect flirting over direct confessions.",
    "💝 순정파(The Devoted Soul)":                  "a person who demonstrates high emotional commitment and consistency. Uses sincere, unadorned language and shows deep empathy. Focuses on building a long-term, stable bond through honest communication and vulnerability.",
    "😇 유죄인간(The Accidental Heartthrob)":       "a person who naturally kind and charming without realizing the romantic impact on others. Uses polite and caring language toward everyone, often leading to unintentional fluttering of hearts or misunderstandings.",
    "🚀 직진형(The Bold Go-Getter)":                "a person who expresses romantic interest directly and immediately. Values transparency and takes the initiative in asking for dates or confessing feelings. Minimal use of metaphors; highly action-oriented and straightforward.",
    "🤔 신중파(The Cautious Observer)":             "a person who suggests slowing down and taking time to get to know each other better before committing. Prefers gradual relationship progression and avoids rushing into romance.",
    "🌹 로맨티스트(The Hopeless Romantic)":         "a person who enjoys poetic and sentimental expressions in daily conversation. Focuses on creating romantic narratives, emotional resonance, and special atmospheres. Values 'the little things' and idealistic romantic gestures."
}

def classify(text: str) -> list:
    """
    두 모델의 결과를 앙상블(평균)하여 연애 캐릭터 유형을 분류합니다.
    반환값: [(유형이름, 점수), ...] 높은 점수 순 정렬
    """
    candidate_labels = list(labels.values())

    # pipeline 실행
    # 모델 A
    result_a = classifier_a(text, candidate_labels)

    # 모델 B
    result_b = classifier_b(text, candidate_labels)

    # 두 모델 점수 -> 딕셔너리로 변환
    scores_a = dict(zip(result_a['labels'], result_a['scores']))
    scores_b = dict(zip(result_b['labels'], result_b['scores']))

    # 앙상블: 두 점수 평균
    desc_to_name = {v: k for k, v in labels.items()}
    output = []
    for desc in candidate_labels:
        avg_score = (scores_a[desc] + scores_b[desc]) / 2
        output.append((desc_to_name[desc], round(avg_score, 4)))

    # 높은 점수 순 정렬
    output.sort(key=lambda x: x[1], reverse=True)
    return output