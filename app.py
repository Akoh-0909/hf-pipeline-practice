import streamlit as st
from classifier import classify

st.set_page_config(
    page_title="💕 연애 캐릭터 분류기",
    page_icon="💕"
)

st.title("💕 내 말투 연애 캐릭터 분류기")
st.write("내가 쓴 문장으로 나의 연애 스타일을 알아보세요!")
st.divider()

text = st.text_area(
    label="문장을 입력하세요",
    placeholder="예) 나 사실 너 많이 좋아하는데 티 안 내려고 했어...",
    height=100
)

if st.button("분석하기 💘"):
    if not text.strip():
        st.warning("문장을 입력해주세요.")
    else:
        with st.spinner("분석 중..."):
            results = classify(text)

        st.divider()
        st.subheader("📊 분류 결과")

        # 1위 유형 강조
        top_label, top_score = results[0]
        st.success(f"당신의 연애 캐릭터는 **{top_label}** 입니다!")

        st.divider()

        # 전체 순위 출력
        for rank, (label, score) in enumerate(results, 1):
            st.write(f"**{rank}위** {label}")
            st.progress(float(score))
            st.caption(f"점수: {score:.4f}")