from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

# 创建对象
db = SQLAlchemy()
migrate = Migrate(db)
mail = Mail()


# 初始化
def config_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
