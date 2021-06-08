import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib.request
import os

client = MongoClient('localhost', 27017)
db = client.winedb


headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}]
baseurl = 'http://www.winenara.com/goods/goods_list.php'

for i in range(1, 9):

        v = '001'
        params = {'page': i, 'cateCd': v}

        response = requests.get(baseurl, params=params, headers=headers[0])

        soup = BeautifulSoup(response.content, 'html.parser')

        descriptions = soup.select(
                '#contents > div > div.content > div.goods_list_item > div.goods_list > div > div > ul > li')

        for desc in descriptions:
                wine_name = desc.select_one('a > strong.item_name').text
                wine_img = desc.select_one('div.item_photo_box > a > img')['src']

                doc = {
                        'wine_name': wine_name,
                        'wine_img': 'http://www.winenara.com'+wine_img,
                        'none':0
                }

                db.winelist1.insert_one(doc)

# 코딩 시작
# 이미지다운로드용

src = list(db.winelist1.find({'none':0},{'_id':False,'none':False}))

for sr in src:
        url = sr['wine_img']
        name = sr['wine_name']
        path = './static/img/'+name+'.jpg'
        urllib.request.urlretrieve(url,path)
