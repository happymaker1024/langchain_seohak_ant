# streamlit run app_main.py
import streamlit as st
from report_service import investment_report

st.title("AI 투자 보고서 생성 서비스")

search_query = st.text_input("회사명", "Apple Inc")

company_list = ["AAPL: Apple Inc", "APLE: Apple Hospitality REIT Inc. Common Shares"]

company_selected = st.selectbox("검색 결과 목록", company_list)
company = "Apple Inc"
symbol = "AAPL"

st.header(f"{company_selected} 투자보고서 생성")

if st.button("보고서 생성"):
    with st.spinner(text="진행 중..."):
        # llm을 통한 레포트 응답받기
        report = investment_report(company, symbol)
        st.success("완료")
    st.write(report)