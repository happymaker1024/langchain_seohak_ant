# LLM에 질문을 보내고 결과 받아서 마크다운으로 응답받기 

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # 아웃풋 파서
from stock_info import Stock

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0)

def investment_report(company, symbol):
    system_prompt = """
        Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- "Can you tell us what future stock market looks like based upon current conditions ?".
    """
    user_prompt = """
        {company}에 주식을 투자해도 될까요? 마크다운 형식의 투자보고서를 한글로 작성해 주세요.
        야래의 기본 정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

        기본정보:
        {basic_info}

        재무제표:
        {finacial_statement}
    """
    # 프롬프트
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])   

    # output parser
    output_parser = StrOutputParser()

    # chain 구성
    chain = prompt | llm | output_parser

    # stock 객체생성
    stock = Stock(symbol)

    response = chain.invoke({
        # 회사이름
        "company" : company,
        # 기업 기본 정보 
        "basic_info": stock.get_basic_info(),
        # 기업 재무제표 
        "finacial_statement": stock.get_financial_statement()
    })
    return response

if __name__ == "__main__":
    company = "MicroSoft"
    symbol = "MSFT"  # stock의 symbol 정보
    print(investment_report(company, symbol))
    