# -*- coding:utf-8 _*-
from .main import main
from .posts import post
from .example import example
from .users import user
from .login import login

# 蓝本配置
DEFAULT_BLUEPRINT = (
    (main, ''),
    (post, ''),
    (example, ''),
    (user, ''),
    (login, ''),
)


# 封装一个函数config_blueprint,完成蓝本的注册
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
