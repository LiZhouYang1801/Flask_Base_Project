from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, ValidationError
from app.models.users import User


class UserForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'name is invalid')])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("用户已存在")
