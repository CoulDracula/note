### 相关文档

react batchUpdate
* http://www.tuicool.com/articles/ABZBve

### 代码集锦

createElement: 
 ```
<RaisedButton linkButton={true}
                        containerElement={<Link to={`/questions/`}/>}
                        label="返回"/>
 ```


#### this.props.children
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

#### react-router 的钩子、IndexRoute、Route、IndexLink、Redirect、通配符等

http://www.ruanyifeng.com/blog/2016/05/react_router.html?utm_source=tool.lu
* 在使用父子组件嵌套子级组件的时候要注意： 父级组件中的{this.props.children} 是显示子级组件的内容的地方，父级组件路由要包含子级组件
路由可以这么写

 ```
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

 ```
<Field>
{ testData &&
<div></div>}
</Field>
 ```
会出现渲染顺序的问题，但是，使用map方法在<Field> 中遍历就不会出现渲染顺序的问题

#### 父子组件数据交流（重点在子级元素向父级元素传递数据）
使用子级组件调用父级组件函数，子级组件state通过函数传递给父级组件state。注意：务必是子级组件的state中某个参数通过函数传递，而不是直接传递子级组件某个参数。
详见http://www.tuicool.com/articles/AzQzEbq

#### 关于父级组件获取子级组件数值
： 使用子级组件调用父级组件函数，子级组件state通过函数传递给父级组件state。注意：务必是子级组件的state中某个参数通过函数传递，而不是直接传递子级组件某个参数。 详见http://www.tuicool.com/articles/AzQzEbq
但是不如redux的store动态传参。mapStateToProps 更好一些