from flask import Flask, jsonify, request
from werkzeug.utils import redirect
import json



app = Flask(__name__)  # 实例化一个类 传入的参数为'__main__'


@app.route("/")  # 装饰器路由 http://127.0.0.1:5000/ 默认是GET格式
def hello_world():
    return jsonify(name='张三', age=18)  # 返回json数据


@app.route("/hey")
def hey_xiaokang():
    return 'hey xiaokang'


@app.route("/params/<int:number>")  # 带路由参数，如果不指定参数类型 默认字符串
def route_params(number):
    return 'result: %s' % (number + number)


@app.route("/baidu")  # 重定向
def baidu():
    return redirect('https://www.baidu.com')


@app.route("/test/my/first", methods=['POST'])  # 定义post接口
def first_post():
    try:
        data = request.get_data()
        data = json.loads(data.decode("utf-8"))
        print(data)
        # get_name = request.json.get("name")  # 获取前端提交的数据
        # get_age = request.json.get("age")
        # if not all([get_age, get_name]):
        #     return jsonify(msg="缺少参数")
        # get_age += 10
        # return jsonify(name=get_name, age=get_age)  # 返回json格式数据
        return data
    except Exception as e:
        print(e)
        return jsonify(msg="出错了啦")


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # 加上host='0.0.0.0'  就是允许所有主机进行访问
