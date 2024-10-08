# 一、网站应该保存在何处？

当你在本地计算机上构建网站时，应该将所有的相关文件放在一个映射出服务器端线上站点文件结构的单独文件夹中。这个文件夹可以放在你喜欢的任何地方，但你应该把它放在能轻易找到的地方，也许是在桌面上，在家目录里，或者在硬盘根目录下。

- 1.选择一个存放网站项目的地方。在你选择的地方，创建一个名为 web-projects（或类似）的新文件夹。这是你所有的网站项目的存放地。
- 2.在这个文件夹中，创建另一个存放你的第一个网站的文件夹。称之为 test-site（或更有想象力的名字）。

 # 二、关于大小写和空格的提示
 你会注意到，在本文中，我们要求你完全用小写字母且不带空格命名文件夹和文件。这是因为：

许多计算机，特别是 Web 服务器，是区分大小写的。因此，假如把你的网站上的一张图片放在 test-site/MyImage.jpg，然后在一个不同的文件中，你试图以 test-site/myimage.jpg 调用该图片，它可能无法工作。
许多情况下，带有空格的文件名会出现问题：
- 在终端中调用命令时，你不得不在带有空格的文件名的周围包裹引号，否则这个路径会解释成两个不同的项。
- 一些编程语言（如 Python）在导入模块文件时，不能很好地处理文件名中的空格。
  
  基于这些原因，最好养成文件夹名和文件名使用小写、不带空格、用连字符分隔单词的习惯，至少直到你清楚自己在做什么的那个时候。那样的话，在接下来的旅程中，你遇到的问题会更少。

 # 三、网站应该使用什么结构？
 在我们创建的任何网站项目中，最常见的是一个主页 HTML 文件和包含图像、样式文件和脚本文件的文件夹。现在让我们创建这些：

-  **`index.html`** ：这个文件一般包含主页内容，也就是用户第一次访问网站时看到的文字和图片。使用文本编辑器，创建一个名为 `index.html` 的新文件，并将其保存在 `test-site` 文件夹内。
- **`images`** 文件夹：这个文件夹包含网站上使用的所有图片。在 `test-site` 文件夹内创建一个名为 `images` 的文件夹。
- **`styles`** 文件夹：这个文件夹包含为内容提供样式的 CSS 代码（例如，设置文本和背景的颜色）。在 `test-site` 文件夹内创建一个名为 `styles` 的文件夹。
- **`scripts`** 文件夹：这个文件夹包含所有用于向网站添加交互功能的 JavaScript 代码（例如，点击时加载数据的按钮）。在 `test-site`文件夹内创建一个名为 `scripts` 的文件夹。

## 一些通用的文件路径规则：

- 若引用的目标文件与 HTML 文件同级，只需直接使用文件名，例如：my-image.jpg。
- 要引用子目录中的文件，请在路径前面写上目录名，再加上一个正斜杠。例如：subdirectory/my-image.jpg。
- 若引用的目标文件位于 HTML 文件的上级，需要加上两个点。举个例子，如果 index.html 在 test-site 的一个子文件夹内，而 my-image.jpg 在 test-site 内，你可以使用 ../my-image.jpg 从 index.html 引用 my-image.jpg。
- 以上方法可以随意组合，比如：../subdirectory/another-subdirectory/my-image.jpg。

