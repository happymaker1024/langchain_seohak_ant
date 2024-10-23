import yfinance as yf
import pandas as pd

class Stock:
    # 생성자
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    # 회사 정보를 수집해서 markdown으로 변경
    def get_basic_info(self):
        basic_info = pd.DataFrame.from_dict(self.ticker.info, orient='index', columns=['Value'])
        return basic_info.loc[['longName', 'marketCap', 'industry', 'sector', 'enterpriseValue']].to_markdown
    
    # 재무제표 수집하기
    def get_financial_statement(self):
        return f"""
            ### Quarterly Income Statement(손익계산서)
            {self.ticker.income_stmt.loc[['Total Revenue', 'Gross Profit', 'Operating Income', 'Net Income']].to_markdown()}

            ### Quarterly Balance Sheet(대차대조표)
            {self.ticker.balance_sheet.loc[['Total Assets', 'Total Liabilities Net Minority Interest', 'Stockholders Equity']].to_markdown()}

            ### Quarterly Cash Flow(현글흐름표)
            {self.ticker.cash_flow.loc[['Operating Cash Flow', 'Investing Cash Flow', 'Financing Cash Flow']].to_markdown()}
        """
    # 주식 거래량
    def get_volume(self):
        return self.ticker.history(period="1mo")["Volume"]
    
if __name__ == "__main__":
    symbol = "MSFT"
    stock = Stock(symbol)

    # print(stock.get_basic_info())
    # print(stock.get_financial_statement())
    print(stock.get_volume())