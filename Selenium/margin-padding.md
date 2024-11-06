# margin
ref: https://developer.mozilla.org/zh-CN/docs/Web/CSS/margin

margin 属性为给定元素设置所有四个（上右下左）方向的外边距属性。
也就是 margin-top、margin-right、margin-bottom 和 margin-left 四个外边距属性设置的简写。

- /* 应用于所有边 */

margin: 1em;
margin: -3px;

- /* 上边下边 | 左边右边 */

margin: 5% auto;

- /* 上边 | 左边右边 | 下边 */

margin: 1em auto 2em;

- /* 上边 | 右边 | 下边 | 左边 */

margin: 2px 1em 0 auto;

/* 全局值 */

margin: inherit;
margin: initial;
margin: unset;

margin 属性接受 1~4 个值。每个值可以是 <length>，<percentage>，或 auto。取值为负时元素会比原来更接近临近元素。

当只指定一个值时，该值会统一应用到全部四个边的外边距上。
指定两个值时，第一个值会应用于上边和下边的外边距，第二个值应用于左边和右边。
指定三个值时，第一个值应用于上边，第二个值应用于右边和左边，第三个则应用于下边的外边距。
指定四个值时，依次（顺时针方向）作为上边，右边，下边，和左边的外边距。


# padding
