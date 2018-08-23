from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_restful import Api
from flask_marshmallow import Marshmallow
# 创建对象
db = SQLAlchemy()
migrate = Migrate(db=db)
api = Api()
mail = Mail()
ma = Marshmallow()


# 初始化
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    api.init_app(app)
    ma.init_app(app)