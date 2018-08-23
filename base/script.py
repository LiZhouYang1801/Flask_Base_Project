from flask import Flask, request, jsonify
from flask_wtf import Form
from wtforms import StringField, FormField, IntegerField
from wtforms.validators import InputRequired
import wtforms_json

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False
wtforms_json.init()


class Address(Form):
    street = StringField('street', validators=[InputRequired()])
    number = IntegerField('number', validators=[InputRequired()])


class User(Form):
    name = StringField('name', validators=[InputRequired()])
    address = FormField(Address, label='address')


@app.route('/', methods=['POST'])
def why_no_work():
    form = User.from_json(request.json)
    print(form.data)

    if form.validate():
        return jsonify(success='YEAH')
    else:
        return jsonify(errors=form.errors)


if __name__ == '__main__':
    # app.run(debug=True)
    import uuid
    import os

    u = uuid.uuid1()
    u_h = uuid.uuid1().hex
    print(u)
    print(u_h, len(u_h))
