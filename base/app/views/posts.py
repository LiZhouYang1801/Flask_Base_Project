from flask import Blueprint, request, jsonify
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from app.extensions import api, db
from app.models.post import Post, Category

post = Blueprint('post', __name__)
category_model_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

post_model_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'pub_date': fields.DateTime,
    'category': fields.List(fields.Nested(category_model_fields)),
}

post_fields = {
    'msg': fields.String(default='ok'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(post_model_fields),
}


# 帖子
class PostListApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=True, help="title必须提供")
        self.parser.add_argument('body', type=str, required=True, help="body必须提供")
        self.parser.add_argument('category_id', type=int, required=True, help="category_id必须提供")
        super(PostListApi, self).__init__()

    @marshal_with(post_fields)
    def get(self):
        category_id = request.args.get("category_id")
        print(category_id, type(category_id))
        if category_id:
            print("*****1")
            posts = Post.query.filter(category_id==int(category_id))
            # posts = Post.query.all()
            print(posts)
            # for p in posts:
            #     print(p)
        #     print("*****1.1")
        # else:
        #     print("*****2")
        #     posts = Post.query.all()
            data = {
                'msg': 'ok',
                'status': 200,
                'data': posts
            }

            return data
        return abort(404)

    @marshal_with(post_fields)
    def post(self):
        args = self.parser.parse_args()
        title = args.get('title', '')
        body = args.get('body', '')
        category_id = args.get('category_id', 0)
        post = Post(title=title, body=body, category_id=category_id)
        db.session.add(post)
        db.session.commit()
        # post = Post.query.all()[-1]
        data = {
            'msg': 'ok',
            'status': 201,
            'data': post,
        }
        return data


# 定义参数解析对象
# parser = reqparse.RequestParser()
# parser.add_argument('id', type=int, required=True, help="id必须提供")
# parser.add_argument('title', type=str, required=False, help="帖子标题")
# parser.add_argument('body', type=str, required=False, help="帖子内容")


class PostApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, required=False, help="ti必须提供")
        self.parser.add_argument('body', type=str, required=False, help="id必须提供")
        super(PostApi, self).__init__()

    @marshal_with(post_fields)
    def get(self, id):
        # args = parser.parse_args()
        # print(args)
        # post_id = args.get('id')
        post = Post.query.get(int(id))
        data = {
            'msg': 'ok',
            'status': 200,
            'data': post,
        }

        return data

    @marshal_with(post_fields)
    def put(self, id):
        args = self.parser.parse_args()
        title = args.get('title')
        body = args.get('body')
        try:
            post = Post.query.get(id)
            if title:
                post.title = title
            if body:
                post.body = body
            db.session.commit()
            data = {
                'msg': 'ok',
                'status': 200,
                'data': post,
            }
            return data

        except:
            db.session.rollback()
            db.session.flush()
            abort(404)

    def delete(self, id):
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return '已删除'


api.add_resource(PostListApi, '/post', endpoint='posts')
# api.add_resource(PostApi, '/post/<int:id>', endpoint='post')

category_fields = {
    'msg': fields.String,
    'status': fields.Integer,
    'data': fields.List(fields.Nested(category_model_fields))
}


# 帖子分类
class PostCategory(Resource):
    @marshal_with(category_fields)
    def get(self):
        '''
        获取所有帖子类别
        :return:
        '''
        categorys = Category.query.all()
        data = {
            'msg': 'ok',
            'status': 200,
            'data': categorys,
        }
        return data


api.add_resource(PostCategory,'/categorys',endpoint="categorys")

@post.route("/cate/<int:id>")
def cate(id):
    posts = Post.query.filter_by(category_id=id)
    # for i in posts:
    #     print(i)
    from app.serilazers import CategorySchema
    cs = CategorySchema()
    data = cs.dump(posts).data

    # return data
    return jsonify(data)