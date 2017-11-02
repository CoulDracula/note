
## ES6




### Promise

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


### …  

...是es6语法的解构   声明多个值，可以是对象或者数组

用来取来es5 中a.splice(b)这种数组/对象添加方法

redux中
```javascript
{
  ...state,
  isDecrementing: true
}
```
因为...state是一个object，包含多个值

example
```javascript
const oldVideoRecords = [1,2,3,4,5]
Const videoRecord=6
return [...oldVideoRecords, videoRecord]  //[1,2,3,4,5,6]

redux中常使用 …state

const oldVideoRecords = state.filter(videoRecord => videoRecord.id != action.videoRecord.id)
return [...oldVideoRecords, action.videoRecord]

```




### es6语法糖

```javascript
链接：https://www.zhihu.com/question/53045668/answer/133210331

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


## es 7 新特性

### async 和await

- async是一个异步操作
- await 只能在async中使用，可以理解为一个同步操作 用来取代 .then()

> async生命是一个异步函数，await使用在异步函数中，只有返回promise对象后才继续执行下一个函数（理论上来说await后面跟着应该是一个promise对象，就算不是也没关系，只是await没有意义罢了）


