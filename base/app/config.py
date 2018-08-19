# -*- coding:utf-8 _*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


# 第一配置基类
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get("SECRET_KEY") or '123456'

    # 数据库公用配置
    # 无警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 发邮件 配置

    # 额外的初始化
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/lzy"


# 测试环境配置
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:passwd@localhost/dbname"


# 生产环境配置
class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:passwd@localhost/dbname"


# 生成一个字典,用来根据字符串找到对应的配置类
config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductConfig,
    'default': DevelopmentConfig
}
