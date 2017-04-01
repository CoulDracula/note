# CSS

## ————常见 css 难点、重点

#### 以下css样式区别

```css
line-height:15px
line-height:15
line-height:1.5em
line-height:150%
```

- px：常见的像素，指15像素
- 无单位：指倍数，现有高度15倍
- em：相对浏览器的字体大小，1em=16px
- %：1.5倍高度

### flex

felx：按比例布局方式
*每个div添加flex：n，则按照flex的值进行按比例纵向排列。如果添加参数：flexDirection: 'row'，则视为横向排列。

justifyContent：对齐方式

- 定义主轴对齐方式（纵向对齐方式）
  - flex-start（默认值）：左对齐
  - flex-end：右对齐
  - center： 居中
  - space-between：两端对齐，项目之间的间隔都相等。
  - space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。

flexDirection 定义主轴方向

-（即项目的排列方向）
  - row（默认值）：主轴为水平方向，起点在左端。
  - row-reverse：主轴为水平方向，起点在右端。
  - column：主轴为垂直方向，起点在上沿。
  - column-reverse：主轴为垂直方向，起点在下沿。

alignItems： 属性定义项目在交叉轴上如何对齐

- 即与主轴交叉的副轴的对齐方式
  - flex-start：交叉轴的起点对齐。
  - flex-end：交叉轴的终点对齐。
  - center：交叉轴的中点对齐。
  - baseline: 项目的第一行文字的基线对齐。
  - stretch（默认值）：如果项目未设置高度或设为auto，将占满整个容器的高度。


### 图像

- px: pixels(像素). 不同设备显示效果相同，一般我们HVGA代表320x480像素，这个用的比较多。
- pt: point，是一个标准的长度单位，1pt=1/72英寸，用于印刷业，非常简单易用；
- dp : 设备独立像素（与像素、设备大小有关）
- dpi :表示分辨率,指每英寸长度上的点数
- ppi : 在图像中每英寸所表达的像素数目
- sp: scaled pixels(缩放像素). 主要用于字体显示best for textsize。