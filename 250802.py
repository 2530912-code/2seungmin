import streamlit as st

st.set_page_config(page_title="Burger Builder 🍔")

st.title("🍔 나만의 버거 만들기")

# 선택지
buns = ["참깨빵", "브리오슈", "바게트"]
patties = ["소고기", "닭고기", "두부"]
toppings = ["양상추", "토마토", "피클", "양파"]
sauces = ["케첩", "마요네즈", "바베큐"]

# 입력 받기
bun = st.radio("1. 빵을 선택하세요:", buns)
patty = st.radio("2. 패티를 선택하세요:", patties)
selected_toppings = st.multiselect("3. 토핑을 선택하세요:", toppings)
sauce = st.selectbox("4. 소스를 선택하세요:", sauces)

# 결과 출력
if st.button("🍔 내 버거 완성!"):
    st.success("당신의 버거가 완성되었습니다!")
    burger = f"[ {bun} + {patty} + {', '.join(selected_toppings)} + {sauce} ]"
    st.markdown(f"### 🍔 `{burger}`")

