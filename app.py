from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
import datetime
import jwt

client = MongoClient('localhost', 27017)
db = client.winelist
app = Flask(__name__)


SECRET_KEY = 'HANGHAE'

#로그인
@app.route('/api/login',methods=['POST'])
def logintest():
    user_id = request.form['id_input']
    user_pw = request.form['pw_input']
    user = db.users.find_one({'user_id':user_id},{'user_pw':user_pw})
    # 체크용프린트
    print(user_id,user_pw)
    #입력받은 정보로 그랩해왔는데 일치하는정보가없어?
    if user is None:
        return jsonify({'result':'false','msg':'로그인에 실패하였습니다.'})
    #그랩해온 정보가 일치하면 페이로드발급
    payload = {
        'id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(token)
    return jsonify({'result':'success','token':token,'usernm':user_id})


# -- index --#
@app.route('/')
def index():
    return render_template('index.html')

# -- login --#
@app.route('/login')
def login():
    return render_template('login.html')

# -- join --#
@app.route('/join')
def join():
    return render_template('join.html')

# @app.route('/main')
# def main():
#     return render_template('main.html')

# crawling
@app.route('/api/list', methods=['GET'])
def show_Wines():
    winelist1 = list(db.winelist1.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'wine_list': winelist1})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
