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
    "🎯 밀당고수(The Master of Push-and-Pull)": "a person who expresses desire to contact someone but deliberately holds back. Uses phrases like 'I want to but I'm scared of coming on too strong'.",
    "💝 순정파(The Devoted Soul)": "a person who uses exclusive devotion language like 'only you', 'nobody else', 'I only see you'. Expresses unconditional loyalty and emotional dependency.",
    "😇 유죄인간(The Accidental Heartthrob)": "a person who denies romantic intent while describing physical contact or close proximity. Uses phrases like 'it didn't mean anything' or 'I just did it naturally'.",
    "🚀 직진형(The Bold Go-Getter)": "a person who uses direct imperative phrases like 'let's date' or 'I like you, go out with me'. No hedging, no metaphors. Immediate and unambiguous romantic proposition.",
    "🤔 신중파(The Cautious Observer)": "a person who explicitly asks for more time before starting a relationship. Uses phrases like 'I need more time' or 'let's not rush'. Focuses on compatibility analysis and logical decision-making rather than emotional impulse.",
    "🌹 로맨티스트(The Hopeless Romantic)": "a person who references nature, scenery, or sensory experiences to express longing. Uses poetic imagery like sunsets, seasons, or shared moments to convey feelings.",
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