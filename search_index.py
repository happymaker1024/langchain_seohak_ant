import meilisearch
import pandas as pd

client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

def search_compay(query):
    return client.index('nasdaq').search(query)


# 자료 서칭을 위한 클래스
class SearchResult:
    def __init__(self, item):
        self.item = item

    # @property 데코레이터, 클래스의 메서드를 마치 속성처럼 사용할 수 있음
    @property    
    def symbol(self):
        return self.item['Symbol']
    
    @property
    def name(self):
        return self.item['Name']
    
    # print() 또는 str()문을 만났을 때 출력형태
    def __str__(self):
        # return f"AAPL: Apple Inc"
        return f"{self.symbol}: {self.name}"

if __name__ == "__main__":

    search_query = "MSFT"

    # 서치 목록 만들기
    # search_data = search_compay(search_query)
    # print(search_data)
    hits = search_compay(search_query)['hits']  # hits 키로 데이터 목록이 만들어져 있음
    # print(hits)

    # Symbol, Name 추출
    # 리스트 내포(list comprehension)로 작성
    search_results = [SearchResult(hit) for hit in hits]
  
    # 위 list comprehension과 동일한 의미
    # search_results = []
    # for hit in hits:
    #     search_results.append(SearchResult(hit))

    # 출력 목록 확인
    for search in search_results:
        print(search)