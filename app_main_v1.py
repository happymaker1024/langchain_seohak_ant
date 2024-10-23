# streamlit run app_main.py
import streamlit as st

st.title("AI 투자 보고서 생성 서비스")

search_query = st.text_input("회사명", "Apple Inc")

company_list = ["AAPL: Apple Inc", "APLE: Apple Hospitality REIT Inc. Common Shares"
]

company = st.selectbox("검색 결과 목록", company_list)

st.header(f"{company} 투자보고서 생성")
st.button("보고서 생성")