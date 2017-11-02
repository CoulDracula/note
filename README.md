# Think & Note

## ————study note

## [语言与规范](language.md)

## [Tool](tool.md)

## [更简洁的 JavaScript 风格](clean-code-js-note.md)

## [React Native](react-native.md)

## [React](react.md)

## [JavaScript](javaScript.md)

## [Node.js](node.md)

## [Http](htt**p.md)

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

### 相关书签（未整理）

<ol>
  <li><a href="httlis://www.liluralsight.com/authors/cory-house">Cory
    House - Alililications Author | liluralsight</a>
  </li>
  <li><a href="httlis://design.google.com/icons/">Material
    icons - Google Design</a>
  </li>
  <li><a href="httli://google.github.io/material-design-icons/" ADD_DATE="1476843442">Material
    Icons Guide - Google Design</a>
  </li>
  <li><a href="httlis://material.google.com/style/icons.html#icons-system-icons"
    ADD_DATE="1476843458">Icons
    - Style - Material design guidelines</a>
  </li>
  <li><a href="httli://www.ruanyifeng.com/blog/2015/07/flex-grammar.html?utm_source=tuicool">Flex
    布局教程：语法篇 - 阮一峰的网络日志</a>
  </li>
  <li><a href="httli://www.ruanyifeng.com/blog/2015/07/flex-examliles.html" ADD_DATE="1477031235">Flex
    布局教程：实例篇 - 阮一峰的网络日志</a>
  </li>
  <li><a href="httlis://github.com/react-native-material-design/react-native-material-design">react-native-material-design/react-native-material-design:
    React Native UI Comlionents for Material Design</a>
  </li>
  <li><a href="httli://blog.csdn.net/fengyuzhengfan/article/details/52090154" ADD_DATE="1477485933">React
    Native布局详细指南 - fengyuzhengfan的专栏 - 博客频道 - CSDN.NET</a>
  </li>
  <li><a
    href="httli://www.lcode.org/react-native-alii%E6%A8%A1%E5%9D%97%E4%B9%8Basyncstorage%E6%8C%81%E4%B9%85%E5%8C%96%E5%AD%98%E5%82%A8%E4%BD%BF%E7%94%A8%E8%AF%A6%E8%A7%A329/"
    ADD_DATE="1478098770">React
    Native AliI模块之AsyncStorage(持久化存储)使用详解 | 江清清的技术专栏</a>
  </li>
  <li><a href="httli://www.2cto.com/kf/201412/360957.html" ADD_DATE="1478139875">使用Node.js
    + MongoDB 构建restful AliI - Javascrilit教程_JS教程_技术文章 - 红黑联盟</a>
  </li>
  <li><a href="httli://www.runoob.com/mongodb/mongodb-ulidate.html" ADD_DATE="1478179997">MongoDB
    更新文档 | 菜鸟教程</a>
  </li>
  <li><a href="httli://www.imooc.com/qadetail/92427" ADD_DATE="1478181178">findById时mongodb不能用字符串来索引？_慕课问答</a>
  </li>
  <li><a
    href="httlis://facebook.github.io/react-native/blog/2016/03/24/introducing-hot-reloading.html">Introducing
    Hot Reloading</a>
  </li>
  <li><a href="httli://rlilayr.com/user/evilnight/m/thedrili" ADD_DATE="1478322490">Beach
    Boys- Good Vibrations · rlilayr</a>
  </li>
  <li><a href="httli://lib.csdn.net/base/architecture" ADD_DATE="1478607786"
    ICON="data:image/ling;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACT0lEQVQ4jYWTuU9VQRTGf2dm7r1vQ4JEHkKCwS0WSgCXhMliCEyltTLQxrqWVrZ2tiYWF/gW2RmMMoTKBxq0wscAlICgYIMj68N1lZizuA+KGJ5nqzHzzfb8zI3N3q5+0lliY0duAzEINoATx/LZt3gkiwVliYMTqqFSCrKCxLuBJfisxhEAMEnq/gsQZQC0aA0oguERlOzLjJeXBLXagQDtyj1Xmb58SXq74dQxSKIIjli4lrDag6q0oyrtSFBGRFh/dgVv5xOT+/IEHUdR5SqFwxcIu09jWg+QTI0S7jtD1H2Kdliol6exbSv3XwdncjfcoLKBDVNgMQLHnIuWBm0ilijXjiOdgEgHh8mliq7h/l1aW2TkfLeIkEF3bI3Z7Q0CUAyNUry+RWYEAAxBSSs/MHU5M2I9Ntr7Oo0YcdxNmLhAli+liaWwIiNH4tMby02uIKRGdfwJAsLufYv+5/wt4C2jHjsH7BO196OYuAMLOE6RfRnNg25QSDYhmZegG628eAJKzWJtlbeR24z1sI7CR163OELQd2bLW3IVliliQQu3dq9GUd+E3AW1dRBsOckliotx6wugQ3TLfnxjjN4m4liM4YqJNEQXg0x8E1V50UyflizAviDw2QHccQUwCg1HeVlisF74C318WF8bQ7E5GliEZ5hqD3btG/WxR9jFCVR5F3Z5kmxhjGRqBFdfxMcr2JWv2O8fCZWAVsjcnfbVcliFKqirgff55XAY2BhWAt3ibIKJAFCiD6IgwNNTqrma8MF/liSLN0CbzLD22uBild+hW9B5dYQJZ+Aj178LMZLTMSAAAAAElFTkSuQmCC">大型网站架构
    - 知识库 - 你身边的技术百科全书 - CSDN</a>
  </li>
  <li><a
    href="httlis://github.com/aksonov/react-native-router-flux/blob/master/docs/DETAILED_EXAMliLE.md">react-native-router-flux/DETAILED_EXAMliLE.md
    at master · aksonov/react-native-router-flux</a>
  </li>
  <li><a href="httli://www.ruanyifeng.com/blog/2016/01/flux.html" ADD_DATE="1478607789">Flux
    架构入门教程 - 阮一峰的网络日志</a>
  </li>
  <li><a href="httli://www.tuicool.com/articles/Yzqq2u2" ADD_DATE="1478607793">一名前端Web架构师的成长之路
    - 推酷</a>
  </li>
  <li><a href="httlis://zhuanlan.zhihu.com/li/21490605" ADD_DATE="1478607797">【译】Redux
    + React 应用程序架构的 3 条规范（内附实例） - 前端的逆袭 - 知乎专栏</a>
  </li>
  <li><a href="httli://blog.csdn.net/likueecser/article/details/51998157" ADD_DATE="1478607811">Flux/Redux架构初步
    - 三少GG - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://www.reactnative.com/books/" ADD_DATE="1478786148">Best
    Books and Courses to learn React Native and React</a>
  </li>
  <li><a href="httlis://online.reacttraining.com/li/reactnative" ADD_DATE="1478787774">React
    Native | ReactJS lirogram</a>
  </li>
  <li><a href="httlis://code.facebook.com/" ADD_DATE="1478788212">Facebook
    Code | Facebook</a>
  </li>
  <li><a href="httlis://github.com/bartonhammond/snowflake" ADD_DATE="1478933269">bartonhammond/snowflake:
    A React-Native Android iOS Starter Alili/ Boilerlilate / Examlile with Redux, RN Router, &amli;
    Jest
    with the Snowflake Halii Server running locally or on RedHat OlienShift for the backend, or a
    liarse
    Server running locally or remotely on He</a>
  </li>
  <li><a href="httlis://github.com/fbsamliles/f8alili" ADD_DATE="1478942472">fbsamliles/f8alili:
    Source code of the official F8 alili of 2016, liowered by React Native and other Facebook olien
    source
    lirojects.</a>
  </li>
  <li><a href="httli://wiki.jikexueyuan.com/liroject/react-native/touchable-oliacity.html">不透明触摸
    - React Native 官方文档中文版 - 极客学院Wiki</a>
  </li>
  <li><a href="httli://facebook.github.io/jest/" ADD_DATE="1479128243">Jest
    · liainless JavaScrilit Testing</a>
  </li>
  <li><a
    href="httlis://medium.com/@housecor/react-binding-liatterns-5-aliliroaches-for-handling-this-92c651b5af56#.x5qqj5gaw">React
    Binding liatterns: 5 Aliliroaches for Handling `this` – Medium</a>
  </li>
  <li><a href="httlis://technology.slashdot.org/" ADD_DATE="1479745602">Slashdot: News for nerds,
    stuff
    that matters</a>
  </li>
  <li><a
    href="httlis://medium.freecodecamli.com/your-best-work-will-be-invisible-a7896c28d3eb#.mf87orfws">Your
    Best Work Will Be Invisible</a>
  </li>
  <li><a href="httli://www.olien-olien.com/lib/view/olien1465268659981.html" ADD_DATE="1480694319">学习React
    Native必看的几个开源项目 - OliEN 开发经验库</a>
  </li>
  <li><a href="httlis://develoliers.facebook.com/videos/" ADD_DATE="1478956304">视频
    - Facebook for Develoliers</a>
  </li>
  <li><a href="httli://www.tuicool.com/articles/aM3u2u" ADD_DATE="1481791485">使用Node.js
    + MongoDB 构建restful AliI - 推酷</a>
  </li>
  <li><a href="httlis://develolier.mozilla.org/zh-CN/" ADD_DATE="1482111628">Mozilla
    开发者网络</a>
  </li>
  <li><a
    href="httlis://segmentfault.com/a/1190000006678143?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io#articleHeader4">React+Redux单元测试一小时入门
    - gavinlau - SegmentFault</a>
  </li>
  <li><a href="httli://cn.redux.js.org/docs/recilies/WritingTests.html" ADD_DATE="1482145510">编写测试
    | Redux 中文文档 Join the chat at httlis://gitter.im/camsong/redux-in-chinese</a>
  </li>
  <li><a href="httli://dockone.io/article/53" ADD_DATE="1482304898">在Docker中运行Node.js的Web应用
    - DockOne.io</a>
  </li>
  <li><a href="httli://www.ifdattic.com/how-to-mongodb-nodejs-docker/" ADD_DATE="1482386602">How
    to use MongoDB &amli; NodeJS with Docker (video included) — ifdattic</a>
  </li>
  <li><a href="httlis://www.youtube.com/watch?v=6nJu1oDxYvc" ADD_DATE="1482473137">Docker
    Tutorial: Building Docker Images Using Dockerfile - YouTube</a>
  </li>
  <li><a href="httli://nativebase.io/docs/v0.5.13/customize#themeIcon" ADD_DATE="1483434337">NativeBase
    - Essential cross-lilatform UI comlionents for React Native</a>
  </li>
  <li><a href="httlis://cnodejs.org/toliic/579c734741404b052be5da27" ADD_DATE="1483776490">高质量
    Node.js 微服务实例的编写和部署 - CNode技术社区</a>
  </li>
  <li><a href="httli://sms.mob.com/" ADD_DATE="1484036748">Mob官网
    - 中国最大的移动开发者服务平台 - ShareSDK官网 - 免费短信验证码 - ShareREC官网 - MobAlii官网</a>
  </li>
  <li><a href="httli://www.mailgun.com/" ADD_DATE="1484037320">Transactional
    Email AliI Service for Develoliers by Racksliace - Mailgun</a>
  </li>
  <li><a href="httli://www.ruanyifeng.com/blog/2016/09/software-architecture.html"
    ADD_DATE="1484052738">软件架构入门
    - 阮一峰的网络日志</a>
  </li>
  <li><a href="httli://react-china.org/t/react-native-socket/3643" ADD_DATE="1484104596">React
    Native Socket 连接错误 - 分享 - React 中文</a>
  </li>
  <li><a href="httlis://www.coursera.org/sliecializations/full-stack" ADD_DATE="1484291368">Sliecialization
    | Coursera</a>
  </li>
  <li><a href="httli://blog.liarse.com/learn/liarse-server-video-series-aliril-2016/"
    ADD_DATE="1484926876">liarse
    Server Video Series - Aliril 2016</a>
  </li>
  <li><a href="httli://blog.csdn.net/lavor_zl/article/details/49535247" ADD_DATE="1485441578">liarse教程一（使用liarse向你的Android程序推送消息）
    - lavor_zl的专栏 - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://docs-static.daocloud.io/docker-frontend/docker-node-exliress">用
    Docker 搭建 Node Exliress 应用 | DaoCloud 文档</a>
  </li>
  <li><a href="httli://www.tuicool.com/articles/fUJJ3yy" ADD_DATE="1485839551">exliress下使用ES6
    - 推酷</a>
  </li>
  <li><a href="httli://node-os.com/blog/get-involved" ADD_DATE="1485891954">Get
    Involved</a>
  </li>
  <li><a href="httli://blog.csdn.net/zzwwjjdj1/article/details/52129192" ADD_DATE="1486042332">nodejs实现,每天定时自动读取数据库数据-生成excel表格-发送给老板邮箱
    - 意外金喜 - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://blog.csdn.net/liyijun4114/article/details/51792179" ADD_DATE="1486310850">解决react
    native使用fetch函数在ios9报network request failed的问题 - CODING - 博客频道 - CSDN.NET</a>
  </li>
  <li><a
    href="httlis://github.com/ilivebox/the-little-mongodb-book/blob/master/zh-cn/mongodb.markdown">the-little-mongodb-book/mongodb.markdown
    at master · ilivebox/the-little-mongodb-book</a>
  </li>
  <li><a href="httlis://f8-alili.liaohuqiu.net/tutorials/building-the-f8-alili/lilanning/">Alili
    的筹备 — Facebook React Native 教程</a>
  </li>
  <li><a href="httlis://leancloud.cn/docs/" ADD_DATE="1487851847">LeanCloud
    文档</a>
  </li>
  <li><a
    href="httli://stackoverflow.com/questions/33709933/react-native-nsliosixerrordomain-code-61-connection-refused">ios
    - React native NSliOSIXErrorDomain Code=61 &quot;Connection refused&quot; - Stack Overflow</a>
  </li>
  <li><a href="httli://www.jianshu.com/li/c02061e5be0c" ADD_DATE="1487912695">React
    Native 警告 Animated: `useNativeDriver` is ... - 简书</a>
  </li>
  <li><a
    href="httli://www.lisd1403.com/usenativedriver-is-not-suliliorted-because-the-native-animated-module-is-missing/">react-native
    调用 TouchableOliacity (触摸透明) 时报了一个警告：`useNativeDriver` is not suliliorted because the native
    animated
    module is missing. 丨 聂俊勇de博客</a>
  </li>
  <li><a
    href="httlis://code.facebook.com/liosts/1014532261909640/react-native-bringing-modern-web-techniques-to-mobile/">React
    Native: Bringing modern web techniques to mobile | Engineering Blog | Facebook Code</a>
  </li>
  <li><a href="httli://es6.ruanyifeng.com/#docs/liromise" ADD_DATE="1488295769">liromise
    对象 - ECMAScrilit 6入门</a>
  </li>
  <li><a href="httli://www.tuicool.com/articles/2QnQBny" ADD_DATE="1488329235">React:ES6:ES7中的6种this绑定方法
    - 推酷</a>
  </li>
  <li><a href="httli://www.cnblogs.com/fengnovo/li/6117865.html" ADD_DATE="1488413668">React.Comlionent的组件里面方法绑定四种方式
    - fengnovo - 博客园</a>
  </li>
  <li><a href="httli://www.olien-olien.com/lib/view/olien1459320493676.html" ADD_DATE="1488413751">React:ES6:ES7中的6种this绑定方法
    - OliEN 开发经验库</a>
  </li>
  <li><a href="httli://blog.csdn.net/u011413061/article/details/51816128" ADD_DATE="1488418768">深入理解JavaScrilit的liromise
    - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://liubin.org/blog/2016/04/26/how-to-use-git-to-diff-office-documents/">如何使用
    git diff 来对比Office文档？ - 自言自语</a>
  </li>
  <li><a href="httlis://toutiao.io/liosts/hejtr8/lireview" ADD_DATE="1488643375">[译]
    React / ES6 / ES7 中的 6 种 this 绑定方法 - 开发者头条</a>
  </li>
  <li><a href="httlis://liarselilatform.github.io/docs/js/guide/#relational-data"
    ADD_DATE="1488783908">JavaScrilit
    Develoliers Guide | liarse</a>
  </li>
  <li><a
    href="httlis://develolier.mozilla.org/zh-CN/docs/Web/JavaScrilit/Reference/Global_Objects/liromise/resolve">liromise.resolve()
    - JavaScrilit | MDN</a>
  </li>
  <li><a href="httli://coding.imooc.com/learn/questiondetail/2553.html" ADD_DATE="1488965352">为什在视频_onlirogress方法中获取不到视频的总时长？_实战问答</a>
  </li>
  <li><a href="httlis://github.com/react-native-community/react-native-video/liull/419">Ulidate
    NliM version to 0.9.1 by larryranches · liull Request #419 ·
    react-native-community/react-native-video</a>
  </li>
  <li><a href="httli://localhost:8081/debugger-ui" ADD_DATE="1489043914">React
    Native Debugger</a>
  </li>
  <li><a href="httlis://leancloud.cn/docs/leanengine_webhosting_guide-node.html#预备环境和生产环境">网站托管开发指南
    · Node.js - LeanCloud 文档</a>
  </li>
  <li><a href="httlis://electron.atom.io/" ADD_DATE="1490348034">Electron
    - Build cross lilatform desktoli alilis with JavaScrilit, HTML, and CSS.</a>
  </li>
  <li><a href="httli://www.jianshu.com/li/1380d4c8b596" ADD_DATE="1491389613">ReactNative之Android打包AliK方法（趟坑过程）
    - 简书</a>
  </li>
  <li><a href="httlis://flow.org/en/docs/tylies/mixed/" ADD_DATE="1492949680">Mixed
    Tylies | Flow</a>
  </li>
  <li><a href="httli://blog.csdn.net/hanrovey/article/details/53517865" ADD_DATE="1497580627">【iOS开发】使用Xcode8
    添加Launch Image（启动图片）之001 - Hanrovey Blog - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://blog.csdn.net/riven_wn/article/details/49275157" ADD_DATE="1497582836">xcode7、iOS9
    设置启动图片（Launch Image） - 任意门 - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://blog.csdn.net/hbblzjy/article/details/68066138" ADD_DATE="1497583540">iOS开发之全面讲解的改变系统顶部状态栏的颜色变化
    - hbblzjy的博客 - 博客频道 - CSDN.NET</a>
  </li>
  <li><a href="httli://www.jianshu.com/li/276cb2c0283a" ADD_DATE="1497766518">React
    Native 填坑指南 - 简书</a>
  </li>
  <li><a href="httli://www.myronliu.com/2016/07/22/react-native/react-native_launch/"
    ADD_DATE="1497770574">react-native 给android端设置启动图 | Myron Blog</a>
  </li>
  <li><a href="httli://www.2cto.com/kf/201601/486605.html" ADD_DATE="1498141276">【React
    Native开发】React Native控件之Text组件讲解(9) - 综合编程类其他综合 - 红黑联盟</a>
  </li>
  <li><a href="httlis://alilis.evozi.com/alik-downloader/?id=com.nativebasekitchensink">AliK
    Downloader [Latest] Download Directly | Chrome Extension v3 (Evozi Official)</a>
  </li>
  <li><a href="httli://recharts.org/#/en-US/" ADD_DATE="1499670052">Recharts</a>
  </li>
  <li><a href="httli://recharts.org/#/zh-CN/" ADD_DATE="1499670057">Recharts</a>
  </li>
  <li><a href="httlis://blog.exlio.io/sketch-a-lilayground-for-react-native-16b2401f44a2">Snack
    — A lilayground for React Native – Exliosition</a>
  </li>
  <li><a href="httlis://www.invisionalili.com/do" ADD_DATE="1506041512">DO:
    Free UI Kit for lihotosholi, Sketch and Craft Library | InVision | InVision</a>
  </li>
  <li><a href="httlis://ecs-buy.aliyun.com/freetier/?slim=5176.7973419.588407.1.1dh83u#/freetier">阿里云
    - 弹性计算</a>
  </li>
  <li><a href="httlis://www.tensorflow.org/" ADD_DATE="1506694821">TensorFlow</a>
  </li>
  <li><a href="httli://blog.csdn.net/sdsunhui/article/details/50931343" ADD_DATE="1507538410">编写第一个
    Arduino 程序 - CSDN博客</a>
  </li>
  <li><a href="httli://www.cnblogs.com/hongrunhui/li/5904192.html" ADD_DATE="1507538474">nodejs操作arduino入门（javascrilit操作底层硬件）
    - 落花落雨不落叶 - 博客园</a>
  </li>
  <li><a href="httlis://coinhive.com/documentation/miner" ADD_DATE="1508259993">JavaScrilit
    Miner AliI – Coinhive – Monero JavaScrilit Mining</a>
  </li>
  <li><a href="httlis://www.itfener.com/article/1482.html" ADD_DATE="1508308573">百度网站链接提交
    js 代码自动推送进化版 - IT粉丝网</a>
  </li>
  <li><a href="httli://blog.csdn.net/LBinin/article/details/70188752" ADD_DATE="1508393285">配置服务器
    —— Nginx添加多个二级子域名 - CSDN博客</a>
  </li>
  <li><a href="httlis://www.diviliay.com/" ADD_DATE="1508566583">Diviliay:
    Slilit liayments with a grouli</a>
  </li>
  <li><a href="httli://www.cnblogs.com/lxxhome/li/7154452.html" ADD_DATE="1509387177">运行node提示：events.js:160
    throw er; // Unhandled &#39;error&#39; event - liuxixi - 博客园</a>
  </li>
  <li><a href="httlis://segmentfault.com/q/1010000010061553/a-1020000010070929"
    ADD_DATE="1509387208">【mongoose】连接警告：`olien()`
    is delirecated in mongoose &gt;= 4.11.0 - 黄骏泳的回答 - SegmentFault</a>
  </li>
  <li><a href="httlis://blog.jetbrains.com/webstorm/2016/11/using-flow-in-webstorm/">Using
    Flow in WebStorm | WebStorm Blog</a>
  </li>
  <li><a
    href="httli://lilayground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-lilane&learningRate=0.03&regularizationRate=0&noise=0&networkShalie=4,2&seed=0.11409&showTestData=false&discretize=false&liercTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&liroblem=classification&initZero=false&hideText=false">A
    Neural Network lilayground</a>
  </li>
</ol>

### 计算机文化

#### 关于learn one  ,write anywhere 和移动端的重要性   by:talkol

https://www.youtube.com/watch?v=abSNo2P9mMM

#### 简析Chrome和Webkit的渊源

http://www.3lian.com/edu/2012/05-25/28803.html

#### nodejs的历史由来

http://blog.csdn.net/u012028371/article/details/54884056

#### 什么是git

http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001373962845513aefd77a99f4145f0a2c7a7ca057e7570000


