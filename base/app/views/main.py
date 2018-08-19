# -*- coding:utf-8 _*-
from flask import Blueprint

# 创建蓝本对象
main = Blueprint('main', __name__)


# 视图函数
@main.route('/index/')
def index():
    return "终于见到你了"
