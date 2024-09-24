import mysql.connector

# 连接数据库
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='person_info'
)

try:
    cursor = connection.cursor()

    # 执行 SQL 语句
    cursor.execute("SELECT * FROM user")

    # 获取结果
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()

