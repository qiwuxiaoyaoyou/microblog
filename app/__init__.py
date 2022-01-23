# -*-codeing = utf-8 -*-
# @Time : 2022-01-16 20:23
# @Author : 齐物逍遥游
# @File : __init__.py
# @Software : PyCharm

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象

login = LoginManager(app)
login.login_view = 'login'
from app import routes,models  #导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
