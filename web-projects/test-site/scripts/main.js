// let myHeading = document.querySelector("h1");
// myHeading.textContent = "Hello world!";
// 首先用 querySelector() 函数获取标题(<h1>Mozilla is cool</h1>)的引用，并把它储存在 myHeading 变量中。
// 之后，把 myHeading 变量的属性 textContent （标题内容）"Mozilla is cool"修改为“Hello world!” 。

// 设置图片切换
let myImage = document.querySelector("img");

myImage.onclick = function () {
  let mySrc = myImage.getAttribute("src");
  if (mySrc === "images/flower.png") {
    myImage.setAttribute("src", "images/yellow-bus.png");
  } else {
    myImage.setAttribute("src", "images/flower.png");
  }
};
// 这里首先把 <img> 元素的引用存放在 myImage 变量里。
// 然后将这个变量的 onclick 事件与一个匿名函数绑定。
// 这个匿名函数每次点击图片时：
// 获取这张图片的 src 属性值。
// 用一个条件句来判断 src 的值是否等于原始图像的路径：
// 如果是，则将 src 的值改为第二张图片的路径，并在 <img> 内加载该图片。
// 如果不是（意味着它已经修改过）, 则把 src 的值重新设置为原始图片的路径，即原始状态。

// 设置个性化欢迎信息
// 获取新按钮和标题的引用
let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

// 个性化欢迎信息设置函数
function setUserName() {
    let myName = prompt("请输入你的名字。");
    if (!myName || myName === null) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
      myHeading.textContent = "Mozilla 酷毙了，" + myName;
    }
  }
//   该函数首先调用了 prompt() 函数，与 alert() 类似会弹出一个对话框。
//   但是这里需要用户输入数据，并在确定后将数据存储在 myName 变量里。
// 如果 myName 没有值或值为 null，就再次从头运行setUserName()。
// 如果有值（上面的表达式结果不为真），就把值存储到 localStorage 并且设置标题。
//   接下来将调用 localStorage API，它可以将数据存储在浏览器中供后续获取。
//   这里用 localStorage 的 setItem() 函数来创建一个'name' 数据项，并把 myName 变量复制给它。
//   最后将 textContent 属性设置为一个欢迎字符串加上这个新设置的名字。

// 初始化代码：在页面初次读取时进行构造工作：
if (!localStorage.getItem("name")) {
    setUserName();
  } else {
    let storedName = localStorage.getItem("name");
    myHeading.textContent = "Mozilla 酷毙了，" + storedName;
  }
//   这里首次使用了取非运算符（逻辑非，用 ! 表示）来检测 'name' 数据是否存在。
//   若不存在，调用 setUserName() 创建。
//   若存在（即用户上次访问时设置过），调用 getItem() 获取保存的名字，像上文的 setUserName() 那样设置 textContent。

// 为按钮设置 onclick 事件处理器：
myButton.onclick = function () {
    setUserName();
  };
  