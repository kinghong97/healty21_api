from flask import Flask
from flask_restx import Api, Resource



app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록




@api.route('/main/<user>&<workout>')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class Product_recommend(Resource):
    def get(self,user,workout):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        hi = f"Hi,{user} enjoy your {workout}"
        ab = [123,423,52,521,32]
        return {"hello": ab}



@api.route('/recommend/user/<user>')
class User_recommend(Resource):
    def get(self,user,workout):
        hi = f"Hi,{user} enjoy your {workout}"
        ab = [123,423,52,521,32]
        return {"hello": ab}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
