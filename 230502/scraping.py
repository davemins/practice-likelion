import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=대전 날씨"

# url에 get 요청을 보내 웹 페이지를 가져온다
response = requests.get(url)

# 가져온 웹 페이지의 html 코드를 다루기 쉽게 변환
soup = BeautifulSoup(response.text, 'html.parser')

result = soup.find('div', class_="temperature_text")

# 현재 온도 출력
print(result.get_text())