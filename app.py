import random

import pymysql
from flask import Flask, request, render_template, redirect, url_for

from init import setting as st

app = Flask(__name__)
# 1. 创建数据库连接

conn = pymysql.connect(**st.MYSQL_CONFIG)


@app.route('/')
def index():
    return 'Hello Flask!'


@app.route('/show_users')
def show_users():
    # users = []
    # sql = f'''
    # select username from user
    # '''
    # with conn.cursor() as cursor:
    #     cursor.execute(sql)
    #     res = cursor.fetchall()
    #     [{},{}]
    users = [{"name": "崔昊元", "age": 17, 'gender': 2}, {"name": "贾靖程", "age": 17, 'gender': 2},
             {"name": "吕梦丽", "age": 17, 'gender': 2}, {"name": "李蓉轩", "age": 17, 'gender': 2}]
    return render_template('show_users.html', users=users)


i = 3


@app.route('/login', methods=['GET', 'POST'])
def login():
    # get请求
    global i
    if request.method == 'GET':
        return render_template('login.html')

    # post请求
    username = request.form.get('username')
    password = request.form.get('password')

    return_value = {
        'status_code': 200,  # 状态码
        'msg': {
            'error_msg': '',  # 错误信息
        }
    }

    # 如果用户名为空，返回错误信息
    if not username:
        return_value['status_code'] = 404
        return_value['msg']['error_msg'] = '用户名不能为空'
        return return_value

    if not password:
        return_value['status_code'] = 404
        return_value['msg']['error_msg'] = '密码不能为空'
        return return_value

        # 判断密码是否为纯数字
    if not password.isdigit():
        return_value['status_code'] = 404
        return_value['msg']['error_msg'] = '密码必须为纯数字'
        return return_value

    # 判断用户名是否满足3-8位
    if len(username) < 3 or len(username) > 8:
        return_value['status_code'] = 404
        return_value['msg']['error_msg'] = '用户名长度不符合要求'
        return return_value

    # 判断密码是否满足4-18位
    if len(password) < 4 or len(password) > 18:
        return_value['status_code'] = 404
        return_value['msg']['error_msg'] = '密码长度不符合要求'
        return return_value

    # 对用户名进行验证
    sql = f'''
    select id from user where username='{username}';
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()  # 获取结果
    if not res:
        return_value['status_code'] = 400
        return_value['msg']['error_msg'] = '用户名不存在'
        return return_value

    # 如果用户名存在，再对用户名和密码一块进行验证
    sql = f'''
    select id from user where username='{username}' and password='{password}';
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()  # 获取结果
    # 如果密码错误
    if not res:
        # return {"status_code":404, "msg":"密码错误！"}
        # 3,2,1,0
        i -= 1
        if i > 0:
            print(i)
            return redirect(url_for('login'))
        else:
            return redirect(url_for('reset_pwd'))
    # 如果密码正确
    return redirect(url_for('show_users'))


@app.route('/reset_pwd', methods=["GET", "POST"])
def reset_pwd():
    if request.method == "GET":
        return render_template("reset_pwd.html")
    username = request.form.get("username")
    password = request.form.get("password")
    sql = f'''
    update user set password = '{password}' where username = '{username}'
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()

    # return {"status_code":200, "msg":"密码重置成功！"}
    return redirect(url_for('login'))


@app.route('/update_pwd', methods=["GET", "POST"])
def update_pwd():
    if request.method == "GET":
        return render_template("update_pwd.html")

    username = request.form.get("username")
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password")
    query_sql = f'''
    select * from user where username='{username}' and password='{old_password}';
    '''
    with conn.cursor() as cursor:
        cursor.execute(query_sql)
        res = cursor.fetchall()
        if not res:
            return {"status_code": 404, "msg": "用户名或密码错误，请重试！"}

    sql = f'''
    update user set password='{new_password}' where username = '{username}';
    '''
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()

    # return {"status_code":200, "msg":"密码重置成功！"}
    return redirect(url_for('login'))


# 创建一个路由名为random_poker的路由
@app.route('/random_poker', methods=['GET', 'POST'])
def random_poker(num=1):
    if request.method == 'GET':
        return render_template('random_poker.html')

    if request.method == 'POST':
        num = request.form.get('num')
        if num:
            num = int(num)
        else:
            num = 1

    # 逻辑需求
    # 1. 抽牌过程中，牌不能重复；
    # 2. 抽到大王/小王，则重新抽牌；
    # 3. 将每次抽牌的总分数进行统计；

    # (1. 生成一副牌
    poker = [f'♥️{_}' for _ in range(1, 14)] + \
            [f'♠️{_}' for _ in range(1, 14)] + \
            [f'♦️{_}' for _ in range(1, 14)] + \
            [f'♣️{_}' for _ in range(1, 14)] + \
            ['🃏大王', '🃏小王']

    # (2. 洗牌
    random.shuffle(poker)

    # (3. 抽牌
    cards = [poker.pop() if card in ['🃏大王', '🃏小王'] else card for card in [poker.pop() for _ in range(num)]]

    # (4. 计算分数
    score = sum([int(card[2:]) if card[2:] != '🃏大王' and card[2:] != '🃏小王' else 0 for card in cards])

    # (5. 返回结果
    return render_template('random_poker.html', cards=cards, score=score, num=num)

    # 结果要求：黑桃4，红桃8，红桃KK，大王，总分数为xx


if __name__ == '__main__':
    app.run(debug=True)
