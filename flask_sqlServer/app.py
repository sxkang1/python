import json
import pymssql
from flask import Flask, jsonify, request
from flask_cors import *  # 利用第三方库解决跨域问题
import logging

app = Flask(__name__)
CORS(app, resources=r'/*')  # 利用第三方库解决跨域问题

logging.basicConfig(
    filename='saveMessage.log',  # 保存文件路径
    filemode='a',  # 保存方式，有 w 和 a 模式，默认不写为追加 a 模式
    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
)


# 注册用户，如果数据库中存在该用户直接返回：已注册
def register(userName, passWorld, other):
    """
    :param userName: 用户名
    :param passWorld: 密码
    :param other: 0表示注册 1表示登录
    :return:
    """
    print(userName, passWorld, other)
    logging.warning('接收到的参数username:%s,password:%s---' % (userName, passWorld))
    host = '.'
    user = 'sa'
    password = 'root'
    database = 'TestSqlServer'

    # sql_select = 'SELECT * FROM testTable1 WHERE id=%d' % id

    with pymssql.connect(host, user, password, database, charset="utf8") as conn:  # 连接数据库
        with conn.cursor(as_dict=True) as cursor:  # 创建游标 操作表文件
            cursor.execute('SELECT * FROM userTables WHERE username=%s', userName)  # 执行sql查询语句
            row = cursor.fetchone()  # 获取一行数据
            print(row)
            logging.warning('读取数据库信息。。。')
            if not row:  # 如果表中不存在该用户 向数据库中添加该用户且返回给前端json格式数据 or 返回前端该用户已经注册
                if other == 0:
                    sql = "INSERT INTO userTables VALUES('%s','%s')" % (userName, passWorld)
                    cursor.execute(sql)
                    conn.commit()
                    data = {
                        "status": "200",
                        "data": [{
                            "msg": "用户%s注册成功。。。" % userName,
                            "state": 200
                        }]
                    }
                    logging.warning("注册用户成功。。。")
                else:
                    data = {
                        "status": "200",
                        "data": [{
                            "msg": "用户名或密码错误。。。",
                            "state": 400
                        }]
                    }
                return data
            else:
                if other == 0:  # 返回前端用户注册信息
                    print(0)
                    data = {
                        "status": "200",
                        "data": [{
                            "msg": "用户%s已注册。。。" % userName,
                            "state": 400
                        }]
                    }
                    return data
                else:  # 校验用户名密码是否正确 且返回登录信息
                    print(type(row))
                    print('name--', row['username'])
                    print('word--', row['passworld'])
                    if row['username'] == userName and row['passworld'] == passWorld:
                        data = {
                            "status": "200",
                            "data": [{
                                "msg": "用户%s登录成功。。。" % userName,
                                "state": 200
                            }]
                        }
                        logging.warning("用户登录成功。。。")
                    else:
                        data = {
                            "status": "200",
                            "data": [{
                                "msg": "用户名或密码错误。。。",
                                "state": 400
                            }]
                        }
                    return data


@app.route("/login", methods=["POST"])
def get_user():
    try:
        _data = request.get_data()  # 获取前端接口数据
        _data = json.loads(_data.decode("utf-8"))  # 解决中文乱码
        _passWorld = _data.get("passWorld")  # 获取接口字段
        _userName = _data.get("userName")
        _other = _data.get("other")
        if not _passWorld and not _userName and not _other:
            return jsonify(msg="缺少参数")
        return jsonify(register(userName=_data['userName'], passWorld=_data['passWorld'], other=_data['other']))
    except Exception as e:
        print('err:', e)
        logging.warning('err---', e)
        return jsonify(msg='出错了')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
