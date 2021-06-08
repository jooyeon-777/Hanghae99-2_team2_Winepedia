from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.winelist


doc = {'user_id':'test123','user_pw':'test'}
db.users.insert_one(doc)

#로그인실험을 위한 계정추가용 파일