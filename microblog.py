# -*-codeing = utf-8 -*-
# @Time : 2022-01-16 21:40
# @Author : 齐物逍遥游
# @File : microblog.py
# @Software : PyCharm

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    app.run(debug=True)