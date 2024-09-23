使用 Python 与 MySQL 进行交互通常可以通过以下步骤实现：

### 1. 安装 MySQL 驱动
你需要安装一个 MySQL 驱动，最常用的是 `mysql-connector-python`。可以通过 pip 安装：

```bash
pip install mysql-connector-python
```

### 2. 连接到 MySQL 数据库
你可以使用以下代码连接到 MySQL 数据库：

```python
import mysql.connector

# 创建数据库连接
connection = mysql.connector.connect(
    host='localhost',       # 数据库主机地址
    user='your_username',   # 数据库用户名
    password='your_password', # 数据库密码
    database='your_database'  # 数据库名称
)

# 创建一个游标对象
cursor = connection.cursor()
```

### 3. 执行查询
你可以使用游标对象执行 SQL 查询。例如，插入数据和查询数据：

```python
# 插入数据
cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", ('value1', 'value2'))
connection.commit()  # 提交事务

# 查询数据
cursor.execute("SELECT * FROM your_table")
results = cursor.fetchall()

for row in results:
    print(row)
```

### 4. 关闭连接
使用完毕后，确保关闭游标和连接：

```python
cursor.close()
connection.close()
```

### 5. 错误处理
为了确保代码的健壮性，可以使用 `try-except` 结构处理可能的错误：

```python
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    # 执行数据库操作
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
```

### 6. 使用 ORM（可选）
如果你希望简化数据库操作，可以使用 ORM（对象关系映射）库，比如 SQLAlchemy：

```bash
pip install SQLAlchemy mysql-connector-python
```

然后可以使用 SQLAlchemy 连接 MySQL 和执行操作：

```python
from sqlalchemy import create_engine

# 创建数据库引擎
engine = create_engine('mysql+mysqlconnector://your_username:your_password@localhost/your_database')

# 使用引擎执行 SQL 语句
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM your_table")
    for row in result:
        print(row)
```

注：可以本机下载mysql workbench（图形界面），连接上虚拟机中的数据库，便于查看数据。
