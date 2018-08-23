from flask import Blueprint, jsonify
from flask_restful import Resource, marshal_with, fields, reqparse
from app.extensions import api, db
from app.models.users import User

user = Blueprint('user', __name__)

user_model_fields = {
    'id': fields.Integer,
    'username': fields.String,
    # 'password': fields.String,
    'email': fields.String,
    'login_time': fields.DateTime,
}
user_data_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'data': fields.List(fields.Nested(user_model_fields),default={})
}


class UserAPi(Resource):
    @marshal_with(user_data_fields)
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class UserListApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help="邮箱必须提供")
        self.parser.add_argument('username', type=str, required=True, help="用户名必须提供")
        self.parser.add_argument('password', type=int, required=True, help="密码必须提供")
        super(UserListApi, self).__init__()

    @marshal_with(user_data_fields)
    def get(self):
        users = User.query.all()
        data = {
            'msg': 'ok',
            'status': 200,
            'data': users,
        }
        return data

    @marshal_with(user_data_fields)
    def post(self):
        args = self.parser.parse_args()
        print(args)
        email = args.get('email')
        username = args.get('username')
        password = str(args.get('password'))
        users = User.query.filter_by(username=username)

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            data = {
                'msg': '用户名已存在',
                'status': 400,
                # 'data': {},
            }
            return data
        user = User(email=email, username=username, password=User().set_password(password))
        db.session.add(user)
        db.session.commit()
        data = {
            'msg': 'ok',
            'status': 201,
            'data': user,
        }
        return data


api.add_resource(UserListApi, '/user')
api.add_resource(UserAPi, '/user/<int:id>')
