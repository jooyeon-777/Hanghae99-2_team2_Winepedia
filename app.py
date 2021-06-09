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
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


#회원가입시 아이디중복확인
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
<<<<<<< HEAD
    user = db.users.find_one({'userid': user_id})
    password_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()
=======
    user = db.users.find_one({'user_id': user_id})
>>>>>>> parent of ffd01e6 (password value normalization)

    # 입력받은 정보로 그랩해왔는데 일치하는정보가없어?
    if user is None:
        return jsonify({'result': 'false', 'msg': '로그인에 실패하였습니다.'})
    # 패스워드 확인
    elif user is not None:
        if user_pw != user['user_pw']:
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

        userinfo = db.users.find_one({'user_id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'user_id': userinfo['user_id']})
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

# deletebtn
@app.route('/api/delete', methods=['POST'])
def delete_wine():
    name_receive = request.form['name_give']
    db.winelist1.delete_one({'wine_name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


# 좋아요 누르면 mywinary로 이동
@app.route('/api/save_wine', methods=['POST'])
def save_wine():
    # 단어 저장하기
    wine_receive = request.form['wine_give'] #wine_give라는 이름으로 보내줄게
    price_receive = request.form['price_give']
    doc = {"wine": wine_receive, "price": price_receive}
    db.winelist1.insert_one(doc)
    return jsonify({'result': 'success', 'msg': 'wine saved'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
