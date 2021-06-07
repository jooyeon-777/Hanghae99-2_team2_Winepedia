from flask import Flask, render_template
from flask_jwt_extended import *

app = Flask(__name__)

# -- 토큰생성을 위한 시크릿키 등륵 --#

app.config.update(
    DEBUG=True,
    JWT_SECRET_KET="HANGHAE2JO"
)

jwt = JWTManager(app)

# -- 테스트용 어드민계정 --#
admin_id = "admin"
admin_pw = "testkey"


# -- 로그인 테스트--#
@app.route("/login", methods=['POST'])
def login_proc():
    # 클라이언트 요청값
    input_data = requests.get_json()
    user_id = input_data['id']
    user_pw = input_data['pw']

    if (user_id == admin_id and user_pw == admin_pw):
        print('admin 로그인 성공')
        return jsonify(
            result="success",
            access_token=create_access_token(identity=user_id,
                                             expires_delta=False)

        )
    else:
       return jsonify(
          result = "땡!"
       )


# -- index --#
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
