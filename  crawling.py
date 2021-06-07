import requests
from bs4 import BeautifulSoup
from soupsieve import select_one

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://http://www.winenara.com/goods/goods_list.php?cateCd=001',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

descriptions = soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li:nth-child(1) > div > div.item_info_cont')

for desc in descriptions:
        wine_name = desc.select_one('div.item_tit_box > a > strong.item_name')
        wine_type = desc.select_one('div.item_tit_box > a > strong:nth-child(2)')
        wine_country = desc.select_one('div.item_tit_box > a > strong:nth-child(4)')
        wine_price = desc.select_one('div.item_money_box > strong')

print(wine_name)