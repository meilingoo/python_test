AJAX（Asynchronous JavaScript and XML）是一种在不重新加载整个网页的情况下，与服务器交换数据并更新部分网页的技术。以下是 AJAX 的基本概念和一个简单的使用示例。

### 基本概念
- **异步**：允许网页与服务器进行异步交互，使用户体验更流畅。
- **数据格式**：通常使用 JSON 格式进行数据传输，但也可以使用 XML 或其他格式。

### 示例：使用 jQuery 的 AJAX
以下是一个简单的示例，演示如何使用 jQuery 发送 AJAX 请求。

#### HTML 代码
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AJAX Example</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>User Info</h1>
    <button id="loadUser">Load User</button>
    <div id="userInfo"></div>

    <script>
        $(document).ready(function() {
            $('#loadUser').click(function() {
                $.ajax({
                    url: '/get_user_info',  // 服务器端处理的 URL
                    type: 'GET',            // 请求类型
                    dataType: 'json',       // 预期的数据类型
                    success: function(data) {
                        // 成功回调，更新页面
                        $('#userInfo').html(`Username: ${data.username}<br>Age: ${data.age}<br>Email: ${data.email}`);
                    },
                    error: function(xhr, status, error) {
                        // 错误处理
                        $('#userInfo').html('Error loading user info.');
                    }
                });
            });
        });
    </script>
</body>
</html>
```

#### Flask 服务器端代码
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    # 假设从数据库中获取用户数据
    user_info = {
        'username': 'JohnDoe',
        'age': 30,
        'email': 'john@example.com'
    }
    return jsonify(user_info)  # 返回 JSON 格式的数据

if __name__ == '__main__':
    app.run(debug=True)
```

### 关键点
1. **jQuery AJAX**：使用 jQuery 的 `$.ajax` 方法来发送请求。
2. **成功和错误处理**：定义 `success` 和 `error` 回调函数来处理响应。
3. **JSON 数据**：使用 Flask 的 `jsonify` 返回 JSON 数据。

通过这些步骤，你可以轻松实现 AJAX 功能，提升用户体验。
