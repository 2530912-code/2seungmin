import streamlit as st

st.title("간단 계산기")

# 사용자 입력 받기
num1 = st.number_input("첫 번째 숫자 입력", value=0)
num2 = st.number_input("두 번째 숫자 입력", value=0)

operation = st.selectbox("연산 선택", ["더하기", "빼기", "곱하기", "나누기"])

if st.button("계산하기"):
    if operation == "더하기":
        result = num1 + num2
    elif operation == "빼기":
        result = num1 - num2
    elif operation == "곱하기":
        result = num1 * num2
    else:  # 나누기
        if num2 == 0:
            st.error("0으로 나눌 수 없습니다!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"결과: {result}")
