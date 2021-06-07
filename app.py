from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import *
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.hanghae
app = Flask(__name__)

doc = {'user_id':'admin','user_pw':'admin'}
db.users.insert_one(doc)

#JWT
app.config.update(DEBUG = True, JWT_SECRET_KEY = "HANGHAE")
jwt = JWTManager(app)

#쿠키
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True

#로그인
@app.route('/login',methods=['POST'])
def logintest():
    user_id = request.form['id_input']
    user_pw = request.form['pw_input']
    user = db.users.find_one({'user_id':user_id},{'user_pw':user_pw})
    # 체크용프린트
    print(user_id,user_pw)
    if user is None:
        return jsonify({'login':False})

    access_token = create_access_token(identity= user_id, expires_delta= False)
    refresh_token = create_refresh_token(identity=user_id)

    resp = jsonify({'login':True})

    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    #체크용프린트
    print(access_token,refresh_token)
    return resp, 200


# -- index --#
@app.route('/')
def index():
    return render_template('index.html')

# -- login --#
@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
