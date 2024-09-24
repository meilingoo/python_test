from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

person_info = Flask(__name__)

# 数据库配置
# person_info.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost/person_info'
# person_info.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(person_info)

# 用于存储个人信息的列表
people = []

# 定义模型，定义一个数据库模型，代表你要存储的信息。例如，如果你要存储用户信息：
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
    
# 连接数据库
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='person_info'
)


@person_info.route('/', methods=['GET', 'POST'])
def index():
     # 创建游标对象
    cursor = connection.cursor()

    # 执行 SQL 语句
    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    return render_template('info.html', users=results)  # 初始加载页面


@person_info.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    age = request.form['age']
    email = request.form['email']
    # 创建游标对象
    cursor = connection.cursor()
    # 使用占位符插入数据
    cursor.execute("INSERT INTO user (username, age, email) VALUES (%s, %s, %s)", (username, age, email))
    connection.commit()  # 提交更改
    cursor.close()
    return redirect(url_for('index'))  # 确保这个视图能加载用户数据 


@person_info.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    # 创建游标对象
    cursor = connection.cursor()
    cursor.execute("DELETE FROM user WHERE id = %s;", (user_id,))  # 确保参数为元组,(user_id,) 中的逗号是必需的，它将 user_id 作为单元素元组传递。
    connection.commit()  # 提交更改
    cursor.close()
    return redirect(url_for('index'))  # 重定向回主页面

@person_info.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    cursor = connection.cursor()
    
    if request.method == 'POST':
        # 从表单中获取数据
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']

        # 更新数据库
        cursor.execute("UPDATE user SET username = %s, age = %s, email = %s WHERE id = %s;", 
                       (username, age, email, user_id))
        connection.commit()  # 提交更改
        cursor.close()
        
        return redirect(url_for('index'))  # 重定向回主页面
    
    # 处理 GET 请求，获取用户信息
    cursor.execute("SELECT username, age, email FROM user WHERE id = %s;", (user_id,))
    result = cursor.fetchone()  # 获取单条记录
    cursor.close()

    if result:
        return render_template('edit_user.html', user=result)  # 渲染编辑页面
    else:
        return "用户未找到", 404  # 处理用户不存在的情况


if __name__ == '__main__':
    person_info.run(host='0.0.0.0', port=5001,debug=True)











# db=pymysql.connect(
#     host="localhost",
#     port=3306,
#     user='root',
#     password="123456",
#     database="person_info",
#     charset='utf8'
# )

# # 3.创建游标对象
# #游标是Python和MySQL数据库交互的对象，只有引入游标后，才能在Python程序中调用SQL命令。
# #在上一步创建好连接对象db之后，只需要调用该连接对象的cursor()方法就可以创建游标。
# # 输入以下命令并回车执行，会返回一个游标对象cursor，用于执行SQL命令并返回MySQL的执行结果。
# # 创建好游标对象，还需要使用该游标对象的execute()方法向MySQL发送SQL命令，MySQL服务器接收后解析SQL语句才能返回结果。
# cursor = db.cursor()

# # #4、执行SQL命令
# # #在上一步创建好游标对象cursor之后，使用该游标对象的execute()方法来执行SQL语句。
# # # 输入以下命令并回车执行，这条SQL语句会被发送到MySQL服务器，但是执行结果并不会立即显示，必须要请求结果。#
# # cursor.execute('show databases')

# # #5.获取执行结果
# # #在上一步执行SQL命令后，可以使用游标对象的fetchone()方法来返回执行结果。输入以下命令并回车执行，将会返回前一条记录。
# # #
# # cursor.fetchone()

# # #5. 关闭游标
# # # Python与数据库的交互完成后，需要使用游标对象的close()方法关闭游标。输入以下命令并回车执行，即可关闭游标。
# # cursor.close()

# # #6.关闭数据库
# # #Python与数据库连接完毕后，需要使用连接对象的close()方法关闭连接。输入以下命令并回车执行，即可关闭连接。
# # db.close()

# #4.提交数据库
# #写操作，需要使用commit提交到数据库
# try:
#     cursor.executemany(sql, data)
# # 　　#或者使用下面代码
#     # for i in range(len(data)):
#     #     cursor.execute(sql,data[i])
# except Exception as e:
#     print(e)
#     db.rollback()#如果提交的sql执行错误，事务回滚
# else:
#     #提交到数据库
#     db.commit()#事务提交，提交后，数据持久化到硬盘中，事务开启是默认开启的
# finally:
#     # 5.关闭
#     cursor.close()
#     db.close()