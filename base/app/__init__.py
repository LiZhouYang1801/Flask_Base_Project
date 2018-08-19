# -*- coding:utf-8 _*-
from flask import Flask, render_template
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint


def config_error_handler(app):
    # 定义全局404错误页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html')


def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 加载Config类里面的配置
    app.config.from_object(config.get(config_name) or 'default')
    # 执行额外的初始化
    config.get(config_name).init_app(app)

    # 加载拓展
    config_extensions(app)

    # 配置蓝本
    config_blueprint(app)

    # 配置爱全局错误处理
    config_error_handler(app)

    # 返回实例对象
    return app
