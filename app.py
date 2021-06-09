import hashlib

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
import datetime
import jwt

client = MongoClient('localhost', 27017)
db = client.winelist
app = Flask(__name__)


SECRET_KEY = 'HANGHAE'


# 회원가입
@app.route('/join/save', methods=['POST'])
def sign_up():
    userid_receive = request.form['userid_give']
    password_receive = request.form['password_give']
    username_receive = request.form['username_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "userid": userid_receive,
        "password": password_hash,
        "username": username_receive,
        "userlikelist": {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
            "14": 0,
            "15": 0,
            "16": 0,
            "17": 0,
            "18": 0,
            "19": 0,
            "20": 0,
            "21": 0,
            "22": 0,
            "23": 0,
            "24": 0,
            "25": 0,
            "26": 0,
            "27": 0,
            "28": 0,
            "29": 0,
            "30": 0,
            "31": 0,
            "32": 0,
            "33": 0,
            "34": 0,
            "35": 0,
            "36": 0,
            "37": 0,
            "38": 0,
            "39": 0,
            "40": 0,
            "41": 0,
            "42": 0,
            "43": 0,
            "44": 0,
            "45": 0,
            "46": 0,
            "47": 0,
            "48": 0,
            "49": 0,

        }
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


# 회원가입시 아이디중복확인
@app.route('/join/check_dup', methods=['POST'])
def check_dup():
    userid_receive = request.form['userid_give']
    exists = bool(db.users.find_one({"userid": userid_receive}))
    return jsonify({'result': 'success', 'exists': exists})


# 로그인
@app.route('/api/login', methods=['POST'])
def logintest():
    user_id = request.form['id_input']
    user_pw = request.form['pw_input']

    user = db.users.find_one({'userid': user_id})
    password_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()

    # 입력받은 정보로 그랩해왔는데 일치하는정보가없어?
    if user is None:
        return jsonify({'result': 'false', 'msg': '로그인에 실패하였습니다.'})
    # 패스워드 확인
    elif user is not None:
        if password_hash != user['password']:
            return jsonify({'result': 'false', 'msg': '로그인에 실패하였습니다.'})
        user_name = user['username']
        payload = {
            'id': user_name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'result': 'success', 'token': token, 'usernm': user_name})


# 세션확인
@app.route('/api/session', methods=['GET'])
def session():
    gettoken = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(gettoken, SECRET_KEY, algorithms=['HS256'])
        userinfo = db.users.find_one({'username': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'user_id': userinfo['username']})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


# -- index --#
@app.route('/')
def index():
    return render_template('index.html')


# -- login --#
@app.route('/login')
def login():
    return render_template('login.html')


# -- logout --#
@app.route('/logout')
def logout():
    return render_template('logout.html')


# -- join --#
@app.route('/join')
def join():
    return render_template('join.html')


# -- mywinery --#
@app.route('/mywinery')
def mywinery():
    return render_template('mywinery.html')

# -- navbar --#    
@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

# crawling
@app.route('/api/list', methods=['GET'])
def show_Wines():
    winelist1 = list(db.winelist1.find({}, {'_id': False}).sort('wine_like', -1))
    return jsonify({'wine_list': winelist1})


# likebtn
@app.route('/api/like', methods=['POST'])
def like_wine():
    name_receive = request.form['name_give']
    target_wine = db.winelist1.find_one({'wine_name': name_receive})
    current_like = target_wine['wine_like']
    new_like = current_like + 1

    db.winelist1.update_one({'wine_name': name_receive}, {'$set': {'wine_like': new_like}})
    return jsonify({'msg': '좋아요완료!'})

# 와인 좋아요 받아오기
@app.route('/api/like', methods=['GET'])
def my_wine():
    name_receive = request.form['name_give']
    target_wine = db.winelist1.find_one({'wine_name': name_receive})
    current_wine_num_receive = target_wine['wine_num']

    test = db.users.find_one({'userlikelist': {current_wine_num_receive:0}})
    if test is None:
        db.users.update_one({'userlikelist': {current_wine_num_receive:0}})
    else:
        db.users.update_one({'userlikelist': {current_wine_num_receive:1}})

    return jsonify({"result": "success", 'msg': '즐겨찾기완료!'})



# deletebtn
@app.route('/api/delete', methods=['POST'])
def delete_wine():
    name_receive = request.form['name_give']
    db.winelist1.delete_one({'wine_name': name_receive})
    return jsonify({'msg': '삭제 완료!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
