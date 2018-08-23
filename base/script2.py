from flask import Flask, jsonify, redirect, url_for
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)


class Cat(Resource):
    def get(self, id=0):
        if id:
            data = {
                "id": id,
                "name": "bill",
                "age": 18,
                "time": datetime.now()
            }
            import anyjson
            data = anyjson(data)
            return jsonify(data)
        return redirect(url_for('index'))

    def post(self):
        pass


@app.route('/')
def index():
    return 'this is index'


api.add_resource(Cat, '/cat', '/cat/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
