
# JavaScript 笔记

## —————来自平日笔记积累

### ES6

### [ES6](es6.md)



#### 注意事项

- 动态创建对象名`person[dateFormat(date, 'dddd')] = newDate`



- date函数 :  `.getMonth（）`获取的月份是0-11


- 对于一个字符串类型的`false`,
`Boolean（“false”）===true   //true`
可以全部string化，判断
如`String(“true’)===String(true)  //true`

- map()是生成新数组，返回值就是数组元素



#### 命名规范

单下划线开头的函数：（_name）
**私有函数**

双下划线 (__prop__)
**暂时未知**
**__prop__ :构造函数的内部类型**

js传递的字符串  \n是无法在html中渲染，可以使用一些函数将\n替换为```<br/>```

#### 为什么
```javascript
链接 ： https://cnodejs.org/topic/56a1d827cd415452622eed07
function add(x){
  return function(y){
    return y + x;
  };
}

var addTwo = add(2);
addTwo(3);          // => 5
add(10)(11);        // => 21
```

#### console

```javascript
console.log('hello');
console.info('信息');
console.error('错误');
console.warn('警告');
```

##### 信息分组

```javascript
console.group("第二组信息");
　　　　console.log("第二组第一条:程序爱好者QQ群： 80535344");
　　　　console.log("第二组第二条:欢迎你加入");
　　    console.groupEnd();
```

 !image2.png!

##### console.dir()

###### 可以显示一个对象所有的属性和方法。

```javascript
var info = {
blog:"http://www.jb51.net",
QQGroup:80535344,
message:"程序爱好者欢迎你的加入"
};
console.dir(info);
```

 !image.png!

##### console.dirxml()

###### 用来显示网页的某个节点（node）所包含的html/xml代码。

```javascript
var info = document.getElementById('info');
console.dirxml(info);
```

##### console.time()和console.timeEnd()

###### 用来显示代码的运行时间。

 ```javascript

console.time("控制台计时器一");
　　for(var i=0;i<1000;i++){
　　　　for(var j=0;j<1000;j++){}
　　}
　　console.timeEnd("控制台计时器一");

```

##### console.profile()

###### 性能分析（Profiler）就是分析程序各个部分的运行时间，

```javascript

console.profile('性能分析器');
　　All();
　　console.profileEnd();

```

 !image3.png!

#### FormData查看不到内容

```javascript

 var data = new FormData();
    data.append('datafile', resource.datafile);
    data.append('author', '131164272');
    data.append('title', '131164272');

```


>当    console.log('formData'); 时，显示为空，因为FormData数据是私有数据，查看需要
> console.log(form.get('datafile'));

### js中的preventDefault与stopPropagation详解

> http://www.jb51.net/article/46379.htm

应用于OT-135的media 和OT-140的workshopVIdeo

```html

<GridTile
            key={item.id}
            title={item.title}
            subtitle={<span>by <b>{item.author_name}</b></span>}
            actionIcon={<IconButton><StarBorder color="white"/></IconButton>} tooltip="star tooltip"
                                    tooltipPosition="top-left"
                                    onClick={(event)=>onStarClick(event,item.id)}
            >
              <StarBorder color="white"/>
            </IconButton>
            }
            style={styles.gridTile}
            onClick={() => onClick(item.id)}
          >
            <img src={item.picture}>
            </img>
          </GridTile>
```

```javascript

 const onStarClick = (event, id)=> {
    event.stopPropagation();
    alert(id);   // list page star action
  };
```

************




#### 函数种类

普通函数
```javascript
function test(){}

const test=()=>{}
```

变量匿名函数
```javascript
const test=function (){
  
}

const test=()=>{}
```

无名称匿名函数
```javascript
function () {
  
}

()=>{}
```

立即执行匿名函数
```javascript
(function (p1) {
    alert(p1);
})(1)
```
#### 闭包  

以下函数为立即执行函数，也叫闭包
```javascript
(function(a){
    console.log(a);   //firebug输出123,使用（）运算符
})(123)
```
