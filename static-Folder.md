css文件和图片都是放在static文件夹里的吗?  

是的，通常在 Flask 项目中，所有静态文件（例如 CSS 文件、JavaScript 文件和图片）都应该放在项目的 `static` 文件夹中。Flask 默认会自动将这个文件夹识别为静态资源目录。

以下是推荐的文件夹结构：

```
/your_flask_project/
├── app.py                # Flask 应用代码
├── templates/            # 存放 HTML 模板文件
│   ├── home.html
│   └── login.html
└── static/               # 存放静态资源文件
    ├── styles/           # 存放 CSS 文件
    │   └── login.css
    ├── images/           # 存放图片文件
    │   └── logo.png
    └── js/               # 存放 JavaScript 文件
        └── app.js
```

### 在 HTML 模板中引用静态文件

通过 `url_for` 函数来引用这些静态文件。示例如下：

- **CSS 文件**：
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='styles/login.css') }}">
  ```

- **图片文件**：
  ```html
  <img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
  ```

- **JavaScript 文件**：
  ```html
  <script src="{{ url_for('static', filename='js/app.js') }}"></script>
  ```

这样设置后，Flask 会根据 `url_for` 函数的路径查找并加载相应的静态文件。
