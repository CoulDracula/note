# React Native 开发

## —————— Android、iOS 开发笔记

### 样例

- 学习、修改案例：https://github.com/CoulDracula/carrying.git
- asyncStorage http://www.tuicool.com/articles/IbqeY33
- android activity文件 https://developer.android.com/guide/topics/manifest/activity-element.html
- 特定代码平台 http://reactnative.cn/docs/0.40/platform-specific-code.html#content

### 笔记

根据像素密度获取指定大小的图片

- 如果应用运行在一个高像素密度的设备上，显示的图片也应当分辨率更高。一个取得缩略图的好规则就是将显示尺寸乘以像素密度比：

#### theme

- 设置组件主题
  - 根据组件（或子组件）提供的api，统一设置样式，事件等，统称设置主题 
  - 主题设置需要组件api支持，对于组件不支持的api使用主题设置暂未尝试
  - 样例在home组件中使用过

#### splice screen

- 程序启动画面，与在xcode中设置的功能相似（暂未成功使用启动画面，在xcode中设置的启动画面能正常使用）

### router

**重中之重**

- 使用的是栈方法，对路由数组栈处理
  - 常用方法 （react-native-navigation-redux-helpers）
      1. pushRoute （为栈增加路由元素）
      1. popRoute （删除顶层路由元素，即返回）
      1. jumpTo
      1. reset
      1. replaceAt

app相关信息设置

- app名称
  - ios下
  - android下 /android/app/src/main/AndroidManifest.xml   /android/app/src/main/res/values/strings.xml
- app图标
  - android下  /android/app/src/maim/res/
  - ios下

### react-native 更新

- 小于0.4.0版本
  - react-native-git-upgrade
- 其他
  - react-native upgrade

### 相关npm包、相关文档

nativebase  http://nativebase.io/
bakery / react-native-navigation-redux-helpers
crazycodeboy / RNStudyNotes （技术总结）
start-react / native-starter-kit

http://www.jianshu.com/p/d0cf1c63a41a

关于本地化存储：

- https://www.youtube.com/watch?v=y9B5BOGdqDE&index=8&list=LL3Bw23NX6tjYJfOdPBtQTHA
- 现在使用的是：
  - http://reactnative.cn/docs/0.40/asyncstorage.html#content

### 错误、知识点总结

常见错误集锦：
- http://bbs.reactnative.cn/topic/130/%E6%96%B0%E6%89%8B%E6%8F%90%E9%97%AE%E5%89%8D%E5%85%88%E6%9D%A5%E8%BF%99%E9%87%8C%E7%9C%8B%E7%9C%8B-react-native%E7%9A%84%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98/13

关于首页（并非启动画面）的渲染方式问题
- 如果使用类似qq的底布ToolBar做该屏幕导航，在该屏幕渲染多种页面，页面之间的切换方式应该如何

关于调用图片名称问题
- 调用的图片require({})图片名称无法使用‘-’、‘@’符号，暂时未知原因，使用的话会报关于char方面的错误

 Invalid prop `component` supplied to `Route`. in Route
- 一般是没有export default

 react native 无法使用react-router-redux的push方法跳转路由
- 跳转路由：
  - 根据不同路由方法调用不同跳转函数

```javascript

    static contextTypes = {
        router: React.PropTypes.object.isRequired,   //用以处理路由
    };

    static defaultProps() {
        return {
            key: '/',    //用于goBack
        };
    }

```

 页面黑屏
- 一般是没有定义背景颜色。不知为何，在使用route之后无法定义全局背景颜色（待解决）

Actions may not have an undefined "type" property. Have you misspelled a constant?
- 暂时不知道，出错在action 的type类型未定义之类的

this refs is getting undefined in method
- 多半是没有绑定方法

发现tcomb-form-native不支持中文输入

疑问：React.createElement()做什么用的




#### 选择菜单的候选项既有遍历的又有默认的标签时

> 参考：
https://github.com/NHSRC/facilities-assessment-android-client/blob/d29531f0d42fd83b966ead27b81a698b4eedfa8f/src/js/views/dashboard/start/AssessmentPicker.js

##### 错误(但是可以用于常规的item列表)：

```html
  <Picker
        iosHeader='选择乐器'
        mode="dropdown"
        selectedValue={this.state.instrument}
        onValueChange={this.selectInstrument.bind(this)}
      >
        <Item label="全部" value="all"/>
        {instruments.length > 0 && instruments.map(
          instrument => {
            return (
              <Item key={instrument.id} label={instrument.get('name')} value={instrument.id}/>
            )
          }
        )}
      </Picker>
```


##### 正确

```html
<Picker
        iosHeader='选择乐器'
        mode="dropdown"
        selectedValue={this.state.instrument}
        onValueChange={this.selectInstrument.bind(this)}
      >
        {pickerItems}
      </Picker>


 const pickerItems = [
      <Item label="全部" value="all"/>].concat(
        instruments.map(
          instrument => {
            return (
              <Item key={instrument.id} label={instrument.get('name')} value={instrument.id}/>
            )
          }
        )
      );
```


