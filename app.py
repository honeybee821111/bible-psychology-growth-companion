import streamlit as st
import google.generativeai as genai
import time # 로딩 스피너를 위해 추가

# --- API 키 설정 ---
# 깃허브에 바로 배포 시 스트림릿 클라우드 또는 다른 PaaS에서 st.secrets를 읽어옵니다.
# 로컬 개발 시에는 .streamlit/secrets.toml 파일에 API_KEY를 설정해야 합니다.
try:
    gemini_api_key = st.secrets["AIzaSyA6d46XMcgFUQbtpeROGZFR_cyx2qf9uQs"]
    genai.configure(api_key=gemini_api_key)
except KeyError:
    st.error("⚠️ API 키를 찾을 수 없습니다. '.streamlit/secrets.toml' 파일 또는 Streamlit Cloud Secrets에 'API_KEY'를 설정해주세요.")
    st.stop() # API 키가 없으면 앱 실행 중지

# --- Gemini 모델 초기화 ---
model = genai.GenerativeModel('gemini-pro')

# --- 1. 앱 기본 설정 ---
st.set_page_config(
    page_title="성경적 심리 성장 동반자",
    page_icon="💖",
    layout="centered"
)

# --- 2. 제목 및 설명 ---
st.title("💖 성경적 심리 성장 동반자")
st.markdown("""
당신의 마음을 나누면, **성경의 지혜와 심리학적 통찰을 결합한 위로 메시지**를 드립니다.
이어서 **깊은 성찰을 위한 맞춤형 질문**을 통해 당신의 내면 성장을 돕습니다.
""")

# --- 3. 사용자 감정/고민 입력 섹션 ---
st.header("1단계: 당신의 마음을 나눠주세요")
user_input = st.text_area(
    "지금 당신을 힘들게 하는 감정이나 고민이 있다면 자유롭게 적어주세요. (예: 요즘 미래가 불안하고, 관계가 힘들어요. 자존감이 낮아지는 것 같아요.)",
    height=150,
    placeholder="예: 요즘 불안하고 미래가 막막하게 느껴져요. 사람들과의 관계가 어려워요."
)

# --- 4. 위로 메시지 생성 버튼 ---
if st.button("메시지 & 질문 받기"):
    if user_input:
        # 로딩 스피너 표시
        with st.spinner("당신의 마음을 깊이 이해하고 있어요... 잠시만 기다려주세요."):
            try:
                # --- AI 프롬프트 구성 ---
                prompt = f"""
                당신은 성경적 지혜와 심리학적 통찰을 결합하여 사람들에게 위로와 성장을 돕는 친절한 동반자입니다.
                사용자가 다음과 같은 감정과 고민을 입력했습니다: "{user_input}"

                사용자의 감정에 깊이 공감하고, 이에 대한 성경적 위로의 메시지를 200-300자 내외로 작성해주세요.
                메시지에는 관련된 성경 구절을 1-2개 포함하고, 간결하게 설명해주세요.

                위로 메시지 다음에는 명확하게 '---' (하이픈 3개)로 구분선을 넣어주세요.

                구분선 다음에는 위로 메시지 및 사용자의 고민과 연결되는 2-3가지의 자기 성찰 질문을 제시해주세요. 질문은 심리학적 관점과 성경적 가치(예: 인내, 용서, 사랑, 믿음, 소망 등)를 담아 사용자가 내면을 깊이 들여다보고 성장할 수 있도록 돕는 질문이어야 합니다. 질문은 번호 매겨서 제시해주세요.

                예시 응답 형식:
                [위로 메시지 내용]
                성경 구절: [성경 구절] ([책 이름] [장]:[절])

                ---

                1. [첫 번째 성찰 질문]
                2. [두 번째 성찰 질문]
                """

                # --- Gemini AI 호출 ---
                response = model.generate_content(prompt)
                ai_response_text = response.text

                # --- AI 응답 파싱 (구분선을 기준으로 위로 메시지와 질문 분리) ---
                if "---" in ai_response_text:
                    comfort_message_raw, growth_questions_raw = ai_response_text.split("---", 1)
                else:
                    # 구분선이 없으면 전체를 메시지로 보고, 질문은 기본 안내 텍스트로 대체
                    comfort_message_raw = ai_response_text
                    growth_questions_raw = "죄송합니다. 현재 성찰 질문을 생성할 수 없습니다. (AI 응답 파싱 오류)"

                # --- 결과 표시 ---
                st.subheader("🌟 당신을 위한 위로의 메시지:")
                st.write(f"**당신이 나눈 고민:** _{user_input}_") # 사용자의 원본 고민을 다시 표시
                st.success(comfort_message_raw) # AI가 생성한 위로 메시지

                st.markdown("---") # 시각적 구분선

                st.subheader("💡 성장을 위한 질문:")
                st.info(growth_questions_raw) # AI가 생성한 성장 질문

                # 선택 사항: 기록 저장 버튼 (이 기능은 추후 구현)
                st.markdown("---")
                st.button("이 메시지와 질문을 기록하기 (미구현)")

            except Exception as e:
                st.error(f"메시지 생성 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요. 오류 내용: {e}")
                st.warning("Google Gemini API 키가 올바르게 설정되었는지, 또는 API 할당량을 초과하지 않았는지 확인해주세요.")

    else:
        st.warning("먼저 당신의 감정이나 고민을 입력해주세요.")

# --- 5. 푸터 (선택 사항) ---
st.markdown("---")
st.markdown("Made with ❤️ by Your Name (or Project Team)")
