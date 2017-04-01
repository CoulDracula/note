# Note

## ————study note

# Think & Note

## [语言与规范](language.md)

## [Tool](tool.md)

## [更简洁的 JavaScript 风格](clean-code-js-note.md)

## [React Native](react-native.md)

## [React](react.md)

## [JavaScript](javaScript.md)

## [Node.js](node.md)

## [Http](http.md)

## [Git](git.md)

## [Develop](develop.md)

## [Mongodb](mongodb.md)

## 零碎笔记

- 收到新数据后`componentWillReceiveProps:function(nextProps){...nextProps}`
- 挂载前`componentWillMount:function(){...可以是state}`
- 挂载后`componentDitMount:function(){...可以是state}`
- 是否更新（true更新）```shouldComponentUpdate:function(nextProps,nextState){return true/false;}```
- 更新dom之前,这时候state等不可以改变`componentWillUpdate:function(nextProps,nextState){...}`
- 更新dom之后 `componentDitUpdate:function(prevProps，pervState){...}`
- 卸载元素时 componentWillUnmount
- es6箭头函数省掉了.bind(this)。使用的时候要注意：

```javascript
//true
setTimeout(function(){}.bind(this),time);

//false
setTimeout(function(){},time).bind(this);
```

## 相关知识收藏

### 计算机文化

#### 关于learn one  ,write anywhere 和移动端的重要性   by:talkol

https://www.youtube.com/watch?v=abSNo2P9mMM

#### 简析Chrome和Webkit的渊源

http://www.3lian.com/edu/2012/05-25/28803.html

#### nodejs的历史由来

http://blog.csdn.net/u012028371/article/details/54884056

#### 什么是git

http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001373962845513aefd77a99f4145f0a2c7a7ca057e7570000

