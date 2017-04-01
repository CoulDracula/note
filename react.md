# React

## 常用 react 技术文档

### 相关文档

react batchUpdate
**http://www.tuicool.com/articles/ABZBve**

*********

### 代码集锦

createElement:

 ```html
<RaisedButton linkButton={true}
                        containerElement={<Link to={`/questions/`}/>}
                        label="返回"/>
 ```


#### this.props.children

```javascript
<WithLabel label="none">
            <TextInput
              autoCapitalize="none"
              style={styles.default}
            />
          </WithLabel>


var WithLabel = React.createClass({
  render: function() {
    return (
      <View style={styles.labelContainer}>
        <View style={styles.label}>
          <Text>{this.props.label}</Text>
        </View>
        {this.props.children}
      </View>
    );
  },
});
```

#### react-router 的钩子、IndexRoute、Route、IndexLink、Redirect、通配符等

http://www.ruanyifeng.com/blog/2016/05/react_router.html?utm_source=tool.lu

> 在使用父子组件嵌套子级组件的时候要注意： 父级组件中的{this.props.children} 是显示子级组件的内容的地方，父级组件路由要包含子级组件

路由可以这么写

```html
<Route path='/workshops' component={WorkshopNavBar} >
      <IndexRoute component={WorkshopListPage}/>
      <Route path=":workshopId">
        <IndexRoute component={WorkshopDetailPage}/>
        <Route path="edit" component={WorkshopPropertyEditPage}/>
      </Route>
    </Route>
 ```

#### 关于redux-form动态添加多条数据参考

 http://redux-form.com/6.0.5/examples/fieldArrays/   关于复选框参考http://redux-form.com/6.0.5/examples/react-widgets/

#### 关于redux-form渲染时加载内容

使用redux-form的initialValue，但是这个要在readxForm api下使用，所以动态传递来的initialValue无法从组件中获取 ，只能从mapStateToProps中获取。 注意组件创建方式不是const 而是let，否则调用reduxForm出错。

#### redux form select

redux form 支持实时显示values，可以通过values判断页面内容是否加载
但是

```html

<Field>
{ testData &&
<div></div>}
</Field>
 ```
会出现渲染顺序的问题，但是，使用map方法在```<Field>``` 中遍历就不会出现渲染顺序的问题

#### 父子组件数据交流（重点在子级元素向父级元素传递数据）

使用子级组件调用父级组件函数，子级组件state通过函数传递给父级组件state。注意：务必是子级组件的state中某个参数通过函数传递，而不是直接传递子级组件某个参数。
详见http://www.tuicool.com/articles/AzQzEbq

#### 关于父级组件获取子级组件数值

> 使用子级组件调用父级组件函数，子级组件state通过函数传递给父级组件state。注意：务必是子级组件的state中某个参数通过函数传递，而不是直接传递子级组件某个参数。 详见http://www.tuicool.com/articles/AzQzEbq
> 但是不如redux的store动态传参。mapStateToProps 更好一些

### 组件嵌套的使用提示

> 当子级组件嵌套在父级组件内，当父级组件被卸载，子级组件也会被卸载。
> 比如dropdown下每个item是一个dialog的链接。dropdown关闭（卸载），相应的dialog也会被卸载。依据dom树处理流程，dialog会比dropdown卸载晚，但是一定会被卸载，无法通过阻止dom树操作顺序而中断卸载。

#### bind

关于bind报错的时候，首先检查是不是一些废弃的绑定函数还遗留，造成全局绑定。

#### 英文error

> There is an internal error in the React performance measurement code. Did not expect componentDidMount timer to start while render timer is still in progress for another instance.

> 报上述错误的时候是组件加载优先顺序的问题，一般是某些函数或者参数命名错误的时候

### React 生命周期

> 简单地说，React Component通过其定义的几个函数来控制组件在生命周期的各个阶段的动作。

在ES6中，一个React组件是用一个class来表示的（具体可以参考官方文档），如下：

```javascript
// 定义一个TodoList的React组件，通过继承React.Component来实现
class TodoList extends React.Component {
  ...
}

这几个生命周期相关的函数有：

```javascript

constructor(props, context);

```

构造函数，在创建组件的时候调用一次。

```javascript

void componentWillMount()

```

在组件挂载之前调用一次。如果在这个函数里面调用setState，本次的render函数可以看到更新后的state，并且只渲染一次。

```javascript

void componentDidMount()

```

在组件挂载之后调用一次。这个时候，子主键也都挂载好了，可以在这里使用refs。

```javascript

void componentWillReceiveProps(nextProps)

```

props是父组件传递给子组件的。父组件发生render的时候子组件就会调用componentWillReceiveProps（不管props有没有更新，也不管父子组件之间有没有数据交换）。

```javascript

bool shouldComponentUpdate(nextProps, nextState)

```

组件挂载之后，每次调用setState后都会调用shouldComponentUpdate判断是否需要重新渲染组件。默认返回true，需要重新render。在比较复杂的应用里，有一些数据的改变并不影响界面展示，可以在这里做判断，优化渲染效率。

```javascript

void componentWillUpdate(nextProps, nextState)

```

shouldComponentUpdate返回true或者调用forceUpdate之后，componentWillUpdate会被调用。

```javascript

void componentDidUpdate()

```

除了首次render之后调用componentDidMount，其它render结束之后都是调用componentDidUpdate。

> componentWillMount、componentDidMount和componentWillUpdate、componentDidUpdate可以对应起来。区别在于，前者只有在挂载的时候会被调用；而后者在以后的每次更新渲染之后都会被调用。


#### ReactElement render()

render是一个React组件所必不可少的核心函数（上面的其它函数都不是必须的）。记住，不要在render里面修改state。

```javascript

void componentWillUnmount()

```

组件被卸载的时候调用。一般在componentDidMount里面注册的事件需要在这里删除。

#### 更新方式

在react中，触发render的有4条路径。

以下假设shouldComponentUpdate都是按照默认返回true的方式。

1. 首次渲染Initial Render
1. 调用this.setState （并不是一次setState会触发一次render，React可能会合并操作，再一次性进行render）
1. 父组件发生更新（一般就是props发生改变，但是就算props没有改变或者父子组件之间没有数据交换也会触发render）
1. 调用this.forceUpdate
1. 下面是我对React组件四条更新路径地总结：

> 注意，如果在shouldComponentUpdate里面返回false可以提前退出更新路径