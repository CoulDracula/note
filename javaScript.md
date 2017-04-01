
# JavaScript 笔记

## —————来自平日笔记积累

### ES6


#### Promise

```javascript
var promise = new Promise(function(resolve, reject) {
  // ... some code

  if (/* 异步操作成功 */){
    resolve(value);
  } else {
    reject(error);
  }
});
```

> http://es6.ruanyifeng.com/#docs/promise

#### es6语法糖

```javascript
作者：颜什么都不记得适
链接：https://www.zhihu.com/question/53045668/answer/133210331
来源：知乎
著作权归作者所有，转载请联系作者获得授权。

const uniq = arr => [...new Set(arr)]

const curry = (f, len = f.length) => (...args) => {
    const sub = args.length
    return sub < len ? curry((...rest) => f(...args, ...rest), len - sub) : f(...args)
}

const compose = (...funcs) => {
    const len = funcs.length
    return len ? (...args) => funcs.slice(0, -1).reduceRight((composed, f) => f(composed), funcs[len - 1](...args)) : arg => arg
}

// ap :: f (a -> b) -> f a -> f b
const ap = curry((funcs, xs) => xs.map(x => funcs.map(f => f(x))).reduce((acc, x) => acc.concat(x), []))

// bind :: m a -> (a -> m b) -> m b
const bind = curry((xs, f) => xs.map(f).reduce((acc, x) => acc.concat(x), []))

const Y = f => (f => f(f))(g => f(x => g(g)(x)))

const sort = Y(f => ([m, ...xs]) => m !== undefined ? [...f(xs.filter(x => x <= m)), m, ...f(xs.filter(x => x > m))] : [])

@connect(mapStateToProps, mapDispatchToProps)
class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            // ...
        }
    }

    async componentDidMount() {
        const data = await ajax({
            // ...
        })
        this.setState({ ...this.state, ...data })
    }

    render() {
        const { foo, bar } = this.props
        return (
            // ...
        )
    }
}
```


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

### es 7 新特性

#### async 和await

- async是一个异步操作
- await 只能在async中使用，可以理解为一个同步操作 用来取代 .then()

> async生命是一个异步函数，await使用在异步函数中，只有返回promise对象后才继续执行下一个函数（理论上来说await后面跟着应该是一个promise对象，就算不是也没关系，只是await没有意义罢了）


