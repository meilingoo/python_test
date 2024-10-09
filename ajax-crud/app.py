from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# 连接数据库
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='person_info',
    autocommit=True #启用自动提交
)

@app.route('/')
def index():
    # 创建游标对象

    cursor = connection.cursor()
    # 执行 SQL 语句
    cursor.execute("SELECT * FROM user")
    results = cursor.fetchall()
    response = []
    i=0
    for user in results:   
        i = i+1 
        updated_user = list(user)  # 将元组转换为列表
        print(updated_user)
        print("===========================")
        updated_user.append(i)
        print(updated_user)
        response.append(updated_user)  # 添加到响应列表
    cursor.close()
    return render_template('index.html', users=response) 

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # 使用 get_json() 解析请求体
    print(data)  # 输出接收到的数据
    
    # 使用 get() 方法，避免 KeyError
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    
    if name is None or age is None or email is None:
        return jsonify({"message": "Missing data"}), 400  # 返回错误信息
    
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO user (username, age, email) VALUES (%s, %s, %s)", (name, age, email))
        # connection.commit()  # 提交更改
        
        # 检查插入是否成功
        if cursor.rowcount == 0:
            return jsonify({"message": "Insert failed"}), 500
        
        # 获取刚插入的用户的 ID
        user_id = cursor.lastrowid
        cursor.execute("SELECT * FROM user WHERE id = %s;", (user_id,))
        new_user = cursor.fetchone()
        cursor.close()
      
        if new_user:
            # 将结果转换为字典格式
            user_info = {
                'id': new_user[0],
                'username': new_user[1],
                'age': new_user[2],
                'email': new_user[3]
            }
            return jsonify(user_info), 201  # 返回新用户数据，状态码201表示资源已创建
        else:
            return jsonify({"message": "User not found"}), 404  # 如果没有找到用户，返回404
        
    except Exception as e:
        print("Error occurred:", e)
        connection.rollback()  # 回滚事务
        return jsonify({"message": "Database error"}), 500  # 返回500错误
        
    finally:
        cursor.close()  # 确保游标被关闭
        
# 如果插入信息打印正确，但数据依然未显示在数据库中，可以考虑以下几个方面：

# 事务管理：确保没有在其他地方回滚事务。检查数据库连接设置，确保自动提交没有被禁用。

# 数据库隔离级别：可能存在隔离级别的问题，导致未提交的数据在查询时不可见。可以尝试调整数据库的隔离级别。

# 错误捕获：在 cursor.execute() 后，检查 cursor.rowcount。如果返回的行数为零，说明没有插入成功。

# 连接关闭：确保在每次操作后正确关闭数据库连接，或者在应用结束时关闭连接。可以在 Flask 应用中使用 teardown_appcontext 来处理连接关闭。

# 数据库权限：确认连接的用户对目标表具有插入权限。    


@app.route('/update_user/<int:user_id>', methods=['POST'])
def update_data(user_id):
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE user SET username = %s, age = %s, email = %s WHERE id = %s;", 
                        (name, age, email, user_id))
        print(data)
        connection.commit()
        return jsonify(data), 200
    except Exception as e:
        connection.rollback()  # 如果出现错误，回滚事务
        print("Error occurred:", e)
        return jsonify({"message": "Failed to update data"}), 500
    finally:
        cursor.close()  # 确保游标被关闭

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM user WHERE id = %s;", (user_id,))
        connection.commit()  # 提交更改
        if cursor.rowcount == 0:
            return jsonify({"message": "User not found"}), 404  # 用户未找到
        return jsonify({"message": "Data deleted"}), 200
    except Exception as e:
        print("Error occurred:", e)
        connection.rollback()  # 回滚事务
        return jsonify({"message": "Failed to delete data"}), 500
    finally:
        cursor.close()  # 确保游标被关闭

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
