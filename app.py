import streamlit as st

# --- 1. 앱 기본 설정 ---
st.set_page_config(
    page_title="성경적 심리 성장 동반자",
    page_icon="💖",
    layout="centered"
)

# --- 2. 제목 및 설명 ---
st.title("💖 성경적 심리 성장 동반자")
st.markdown("""
당신의 감정과 고민을 나누면, 성경적 위로와 심리적 통찰을 담은 메시지를 드립니다.
그리고 깊은 성찰을 위한 맞춤형 질문을 통해 당신의 내면 성장을 돕습니다.
""")

# --- 3. 사용자 감정/고민 입력 섹션 ---
st.header("1단계: 당신의 마음을 나눠주세요")
user_input = st.text_area(
    "지금 당신을 힘들게 하는 감정이나 고민이 있다면 자유롭게 적어주세요.",
    height=150,
    placeholder="예: 요즘 불안하고 미래가 막막하게 느껴져요. 사람들과의 관계가 어려워요."
)

# --- 4. 위로 메시지 생성 버튼 ---
if st.button("위로 메시지 받기"):
    if user_input:
        # --- 더미(Dummy) 응답 로직 (AI API 연동 전) ---
        st.subheader("당신을 위한 위로의 메시지:")
        st.write(f"**당신이 나눈 고민:** _{user_input}_")
        st.success("당신의 마음을 이해합니다. 잠시 후, 당신을 위한 성경적 위로와 심리적 통찰이 담긴 메시지가 여기에 나타날 것입니다. 이 메시지는 당신의 내면을 치유하고 힘을 줄 것입니다.")

        st.markdown("---") # 구분선
        st.subheader("2단계: 성장을 위한 질문")
        st.info("위로 메시지에 이어, 당신의 성장을 돕기 위한 맞춤형 질문이 여기에 제시될 것입니다. 이 질문들은 당신이 스스로를 깊이 돌아보고, 성경적 가치를 삶에 적용하는 데 도움을 줄 것입니다.")
        st.write("질문 예시: '이 상황에서 당신이 발견할 수 있는 성경적 희망은 무엇일까요?'")

    else:
        st.warning("먼저 당신의 감정이나 고민을 입력해주세요.")

# --- 5. 푸터 (선택 사항) ---
st.markdown("---")
st.markdown("Made with ❤️ by Your Name (or Project Team)")
