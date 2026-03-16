from classifier import classify

def main():
    print("=" * 50)
    print("💕 내 말투 연애 캐릭터 분류기 💕")
    print("=" * 50)
    print("종료하려면 'q' 또는 'quit'을 입력하세요.")
    print()

    while True:
        text = input("문장을 입력하세요 > ").strip()

        # 종료 조건
        if text.lower() in ['q', 'quit', '종료']:
            print("종료합니다.")
            break

        # 빈 입력 처리
        if not text:
            print("문장을 입력해주세요.\n")
            continue

        # 분류 실행
        print("\n분석 중...\n")
        results = classify(text)

        # 결과 출력
        print("[ 분류 결과 ]")
        for rank, (label, score) in enumerate(results, 1):
            bar = "█" * int(score * 20)
            print(f"{rank}위 {label} | {bar} {score:.4f}")

        print()

if __name__ == "__main__":
    main()