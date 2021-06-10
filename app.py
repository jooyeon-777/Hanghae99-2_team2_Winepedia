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
    a = False
    doc = {
        "userid": userid_receive,
        "password": password_hash,
        "username": username_receive,
        "0": a,
        "1": a,
        "2": a,
        "3": a,
        "4": a,
        "5": a,
        "6": a,
        "7": a,
        "8": a,
        "9": a,
        "10": a,
        "11": a,
        "12": a,
        "13": a,
        "14": a,
        "15": a,
        "16": a,
        "17": a,
        "18": a,
        "19": a,
        "20": a,
        "21": a,
        "22": a,
        "23": a,
        "24": a,
        "25": a,
        "26": a,
        "27": a,
        "28": a,
        "29": a,
        "30": a,
        "31": a,
        "32": a,
        "33": a,
        "34": a,
        "35": a,
        "36": a,
        "37": a,
        "38": a,
        "39": a,
        "40": a,
        "41": a,
        "42": a,
        "43": a,
        "44": a,
        "45": a,
        "46": a,
        "47": a,
        "48": a,
        "49": a,
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
        return jsonify({'result': 'fail', 'msg': '로그인에 실패하였습니다.'})
    # 패스워드 확인
    elif user is not None:
        if password_hash != user['password']:
            return jsonify({'result': 'fail', 'msg': '로그인에 실패하였습니다.'})
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
    return render_template('winery.html')


# -- navbar --#
@app.route('/navbar')
def navbar():
    return render_template('navbar.html')


# 와이너리용 쇼와인
@app.route('/api/favlist', methods=['GET'])
def show_favWines():
    winelist1 = list(db.winelist1.find({}, {'_id': False}))
    gettoken = request.cookies.get('mytoken')  # 토큰가져옴
    payload = jwt.decode(gettoken, SECRET_KEY, algorithms=['HS256'])  # 토큰해독
    userinfo = db.users.find_one({'username': payload['id']}, {'_id': 0})[
        'username']  # 토큰에서 id값(유저닉네임)을 가져온뒤 userinfo변수에 저장
    # user변수에 해당유저좋아요테이블저장
    # 필터값에 변수가 안들어가서...노가다
    user0 = db.users.find_one({'username': userinfo}, {'_id': False, '0': True})['0']
    user1 = db.users.find_one({'username': userinfo}, {'_id': False, '1': True})['1']
    user2 = db.users.find_one({'username': userinfo}, {'_id': False, '2': True})['2']
    user3 = db.users.find_one({'username': userinfo}, {'_id': False, '3': True})['3']
    user4 = db.users.find_one({'username': userinfo}, {'_id': False, '4': True})['4']
    user5 = db.users.find_one({'username': userinfo}, {'_id': False, '5': True})['5']
    user6 = db.users.find_one({'username': userinfo}, {'_id': False, '6': True})['6']
    user7 = db.users.find_one({'username': userinfo}, {'_id': False, '7': True})['7']
    user8 = db.users.find_one({'username': userinfo}, {'_id': False, '8': True})['8']
    user9 = db.users.find_one({'username': userinfo}, {'_id': False, '9': True})['9']
    user10 = db.users.find_one({'username': userinfo}, {'_id': False, '10': True})['10']
    user11 = db.users.find_one({'username': userinfo}, {'_id': False, '11': True})['11']
    user12 = db.users.find_one({'username': userinfo}, {'_id': False, '12': True})['12']
    user13 = db.users.find_one({'username': userinfo}, {'_id': False, '13': True})['13']
    user14 = db.users.find_one({'username': userinfo}, {'_id': False, '14': True})['14']
    user15 = db.users.find_one({'username': userinfo}, {'_id': False, '15': True})['15']
    user16 = db.users.find_one({'username': userinfo}, {'_id': False, '16': True})['16']
    user17 = db.users.find_one({'username': userinfo}, {'_id': False, '17': True})['17']
    user18 = db.users.find_one({'username': userinfo}, {'_id': False, '18': True})['18']
    user19 = db.users.find_one({'username': userinfo}, {'_id': False, '19': True})['19']
    user20 = db.users.find_one({'username': userinfo}, {'_id': False, '20': True})['20']
    user21 = db.users.find_one({'username': userinfo}, {'_id': False, '21': True})['21']
    user22 = db.users.find_one({'username': userinfo}, {'_id': False, '22': True})['22']
    user23 = db.users.find_one({'username': userinfo}, {'_id': False, '23': True})['23']
    user24 = db.users.find_one({'username': userinfo}, {'_id': False, '24': True})['24']
    user25 = db.users.find_one({'username': userinfo}, {'_id': False, '25': True})['25']
    user26 = db.users.find_one({'username': userinfo}, {'_id': False, '26': True})['26']
    user27 = db.users.find_one({'username': userinfo}, {'_id': False, '27': True})['27']
    user28 = db.users.find_one({'username': userinfo}, {'_id': False, '28': True})['28']
    user29 = db.users.find_one({'username': userinfo}, {'_id': False, '29': True})['29']
    user30 = db.users.find_one({'username': userinfo}, {'_id': False, '30': True})['30']
    user31 = db.users.find_one({'username': userinfo}, {'_id': False, '31': True})['31']
    user32 = db.users.find_one({'username': userinfo}, {'_id': False, '32': True})['32']
    user33 = db.users.find_one({'username': userinfo}, {'_id': False, '33': True})['33']
    user34 = db.users.find_one({'username': userinfo}, {'_id': False, '34': True})['34']
    user35 = db.users.find_one({'username': userinfo}, {'_id': False, '35': True})['35']
    user36 = db.users.find_one({'username': userinfo}, {'_id': False, '36': True})['36']
    user37 = db.users.find_one({'username': userinfo}, {'_id': False, '37': True})['37']
    user38 = db.users.find_one({'username': userinfo}, {'_id': False, '38': True})['38']
    user39 = db.users.find_one({'username': userinfo}, {'_id': False, '39': True})['39']
    user40 = db.users.find_one({'username': userinfo}, {'_id': False, '40': True})['40']
    user41 = db.users.find_one({'username': userinfo}, {'_id': False, '41': True})['41']
    user42 = db.users.find_one({'username': userinfo}, {'_id': False, '42': True})['42']
    user43 = db.users.find_one({'username': userinfo}, {'_id': False, '43': True})['43']
    user44 = db.users.find_one({'username': userinfo}, {'_id': False, '44': True})['44']
    user45 = db.users.find_one({'username': userinfo}, {'_id': False, '45': True})['45']
    user46 = db.users.find_one({'username': userinfo}, {'_id': False, '46': True})['46']
    user47 = db.users.find_one({'username': userinfo}, {'_id': False, '47': True})['47']
    user48 = db.users.find_one({'username': userinfo}, {'_id': False, '48': True})['48']
    user49 = db.users.find_one({'username': userinfo}, {'_id': False, '49': True})['49']
    booleanarr = []
    booleanarr.append(user0)
    booleanarr.append(user1)
    booleanarr.append(user2)
    booleanarr.append(user3)
    booleanarr.append(user4)
    booleanarr.append(user5)
    booleanarr.append(user6)
    booleanarr.append(user7)
    booleanarr.append(user8)
    booleanarr.append(user9)
    booleanarr.append(user10)
    booleanarr.append(user11)
    booleanarr.append(user12)
    booleanarr.append(user13)
    booleanarr.append(user14)
    booleanarr.append(user15)
    booleanarr.append(user16)
    booleanarr.append(user17)
    booleanarr.append(user18)
    booleanarr.append(user19)
    booleanarr.append(user20)
    booleanarr.append(user21)
    booleanarr.append(user22)
    booleanarr.append(user23)
    booleanarr.append(user24)
    booleanarr.append(user25)
    booleanarr.append(user26)
    booleanarr.append(user27)
    booleanarr.append(user28)
    booleanarr.append(user29)
    booleanarr.append(user30)
    booleanarr.append(user31)
    booleanarr.append(user32)
    booleanarr.append(user33)
    booleanarr.append(user34)
    booleanarr.append(user35)
    booleanarr.append(user36)
    booleanarr.append(user37)
    booleanarr.append(user38)
    booleanarr.append(user39)
    booleanarr.append(user40)
    booleanarr.append(user41)
    booleanarr.append(user42)
    booleanarr.append(user43)
    booleanarr.append(user44)
    booleanarr.append(user45)
    booleanarr.append(user46)
    booleanarr.append(user47)
    booleanarr.append(user48)
    booleanarr.append(user49)
    return jsonify({'likelist':booleanarr,'wine_list': winelist1})  # 정보요청한 유저 좋아요 테이블을 함께보냄


# 쇼와인 원본
@app.route('/api/list', methods=['GET'])
def show_Wines():
    winelist1 = list(db.winelist1.find({}, {'_id': False}).sort('wine_like', -1))
    return jsonify({'wine_list': winelist1})


# likebtn
@app.route('/api/like', methods=['POST'])
def like_wine():
    t = True
    f = False
    gettoken = request.cookies.get('mytoken')  # 토큰가져옴
    payload = jwt.decode(gettoken, SECRET_KEY, algorithms=['HS256'])  # 토큰해독
    userinfo = db.users.find_one({'username': payload['id']}, {'_id': 0})[
        'username']  # 토큰에서 id값(유저닉네임)을 가져온뒤 userinfo변수에 저장
    user = db.users.find_one({'username': userinfo})  # user변수에 해당유저테이블정보 저장
    num_receive = request.form['num_give']  # 와인넘버를 넘겨받음
    name_receive = request.form['name_give']  # 와인이름을 넘겨받음
    target_wine = db.winelist1.find_one({'wine_name': name_receive})  # 좋아요가 눌린 와인테이블넘겨받음
    current_like = target_wine['wine_like']  # 와인좋아요개수를 넘겨받음
    # user[num_receive]는 유저가 해당와인을 좋아요했는지 확인
    if user[num_receive] == f:  # 만약 좋아요가 안된상태라면
        db.users.update_one({'username': userinfo}, {'$set': {num_receive: t}})  # db를 좋아요한상태로 업데이트함
        new_like = current_like + 1  # like수를 한개올려준뒤
        db.winelist1.update_one({'wine_name': name_receive}, {'$set': {'wine_like': new_like}})  # like 개수를 업데이트
        return jsonify({'msg':'좋아요완료!'})
    else:  # 만약 좋아요가 눌린상태라면
        db.users.update_one({'username': userinfo}, {'$set': {num_receive: f}})  # db를 좋아요안한상태로 업데이트함
        new_like = current_like - 1  # like수를 한개내려준뒤
        db.winelist1.update_one({'wine_name': name_receive}, {'$set': {'wine_like': new_like}})  # like 개수를 업데이트
        return jsonify({'msg':'좋아요가 취소되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
