# streamlit run app_main.py
import streamlit as st
from report_service import investment_report
from stock_info import Stock
from search_index import search_compay, SearchResult

st.title("AI 투자 보고서 생성 서비스")

search_query = st.text_input("회사명", "Apple Inc")

# 서치 목록 만들기
hits = search_compay(search_query)['hits']  # hits 키로 데이터 목록이 만들어져 있음
search_results = [SearchResult(hit) for hit in hits]

company_selected = st.selectbox("검색 결과 목록", search_results)

# company = "Apple Inc"
# symbol = "AAPL"

# tab으로 구분해서 보이기
tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 시각화
with tab1:
    st.header(f"{company_selected}의 6개월 주식 거래량 ")
    stock = Stock(company_selected.symbol)
    volume = stock.get_volume()
    st.line_chart(volume)

# 투자보고서 생성
with tab2:
    st.header(f"{company_selected} 투자보고서 생성")
    if st.button("보고서 생성"):
        with st.spinner(text="진행 중..."):
            # llm을 통한 레포트 응답받기
            report = investment_report(company_selected.name, company_selected.symbol)
            st.success("완료")
        st.write(report)