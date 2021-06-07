import requests
from bs4 import BeautifulSoup

headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}]
baseurl = 'http://www.winenara.com/goods/goods_list.php'


for i in range(1, 9):

        v = '001'
        params = {'page': i, 'cateCd': v}

        response = requests.get(baseurl, params = params, headers = headers[0])

        soup = BeautifulSoup(response.content, 'html.parser')

        descriptions = soup.select('#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li')

        for desc in descriptions:
                wine_name = desc.select_one('a > strong.item_name')
                wine_type = desc.select_one('a > strong')
                wine_country = desc.select_one('a > strong:nth-child(4)')
                wine_price = desc.select_one('div.item_money_box > strong > span')
                wine_img = desc.select_one('div.item_photo_box > a > img')['src'] # 이미지 링크 가져왔음
        
                print(wine_name)
