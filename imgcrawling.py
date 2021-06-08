import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib.request

client = MongoClient('localhost', 27017)
db = client.winedb

#차단 우회를 위한 헤더설정
headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}]
baseurl = 'http://www.winenara.com/goods/goods_list.php'

for i in range(1, 9):

        v = '001'
        params = {'page': i, 'cateCd': v}

        response = requests.get(baseurl, params=params, headers=headers[0])

        soup = BeautifulSoup(response.content, 'html.parser')

        descriptions = soup.select(
                '#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li')

        #이미지저장 간편화를 위한 크롤링

        for desc in descriptions:
                wine_name = desc.select_one('a > strong.item_name').text
                wine_img = desc.select_one('div.item_photo_box > a > img')['src']
                doc = {
                        'wine_name': wine_name,
                        'wine_img': 'http://www.winenara.com'+wine_img,
                        'none':0
                }

                db.winelist1.insert_one(doc)


# 이미지다운로드용

src = list(db.winelist1.find({'none':0},{'_id':False,'none':False}))

#이미지링크와 와인이름을 db에 저장한뒤 해당 이미지를 와인이름.jpg로 저장하기

for sr in src:
        url = sr['wine_img']
        name = sr['wine_name']
        path = './static/img/'+name+'.jpg'
        urllib.request.urlretrieve(url,path)
