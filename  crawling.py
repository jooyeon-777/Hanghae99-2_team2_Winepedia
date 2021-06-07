import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 크롬드라이버를 경로를 입력해서 연결합니다.
# 현재 스크립트와 같은 폴더에 있다면 경로를 따로 입력하지 않아도 됩니다.
driver = webdriver.Chrome()


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EC%99%80%EC%9D%B8&ctgId=6000099422&ctgLv=3&ctgLast=Y&parentCtgId=6000099420',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

descriptions = soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li:nth-child(1) > div > div.item_info_cont')

for desc in descriptions:
        wine_name = desc.select_one('div.item_tit_box > a > strong.item_name')
        wine_type = desc.select_one('div.item_tit_box > a > strong:nth-child(2)')
        wine_country = desc.select_one('div.item_tit_box > a > strong:nth-child(4)')
        wine_price = desc.select_one('div.item_money_box > strong')

print(wine_name)