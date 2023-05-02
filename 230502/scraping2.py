import requests
from bs4 import BeautifulSoup

Constellation = input("\n별자리 : ")

url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=" + Constellation

# url에 get 요청을 보내 웹 페이지를 가져온다
response = requests.get(url)

# 가져온 웹 페이지의 html 코드를 다루기 쉽게 변환
soup = BeautifulSoup(response.text, 'html.parser')

result = soup.find('p', class_="text _cs_fortune_text")

# 현재 온도 출력
print('\n'+result.get_text()+'\n')