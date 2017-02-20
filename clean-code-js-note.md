
# 更简洁的 JavaScript 风格

## 学习来自[clean-code-js](https://github.com/alivebao/clean-code-js)

## 变量
### 使用有意义，可读性好的变量名
对变量的定义要意义，不要起一些没有实际意义的临时名称，变量名称最好是对应的英文名称

### 使用 ES6 的 const 定义常量
var定义的变量，对应es6的let，是可以在定以后修改的

const定义的是常量，在定义之后无法修改

为确保函数的健壮性，能使用const的时候不使用let

### 对功能类似的变量名采用统一的命名风格
统一代码风格，比如变量和函数名使用驼峰命名法（驼峰命名内容为对应的英文名称），css类名等使用首字母大写命名法

### 使用易于检索名称
变量名要简介，有意义，易于检索

对一些常量的string定义的时候常量要有一定的名称意义，不能直接定义一个如：'const i = 2333'，可以定义一些如
```javascript
var MINUTES_IN_A_YEAR = 525600;
```

### 使用说明变量(即有意义的变量名
  对于定义的内容，能够拆分的就不要一次性把所有内容在一个函数或变量中定义出来，
  特别是在函数调用该变量的时候，变量请提前定义好，而不是在函数定义的参数中定义

```javascript
const cityStateRegex = /^(.+)[,\\s]+(.+?)\s*(\d{5})?$/;
const match = cityStateRegex.match(cityStateRegex)
```

### 不要绕太多的弯子
显式优于隐式。
函数参数的定义最好也有意义，不用定义一个'i'、'j'等无意义或不容易想到意义的定义

### 避免重复的描述
函数名特别是类名定义不要意义重复，比如不要出现
```javascript
var car={
  carType:'test'
}
```

### 避免无意义的条件判断
能够在函数中确保的内容，就不要定义无意义的条件判断，不要单纯的堆积代码量


## **函数**
### 函数参数 (理想情况下应不超过 2 个)
函数的参数不要过多，最好不要超过两格，如果需要的参数过多，可以柯里化。

函数参数过多以为这函数的定义和设计有缺陷

### 函数功能的单一性
每个函数功能要单一，不要处理多项不相干事情，不同事情使用不同的独立函数，各司其职

### 函数名应明确表明其功能
函数名定义和变量名定义相似，不要使用无意义的定义，一般组合为动词，用来表述所做的事情

### 函数应该只做一层抽象
不要使用多层抽象，每个函数应具有单一性，可以使用组合函数的方式处理具有一定耦合性的工作。
多层抽象的函数要及时拆分

### 移除重复的代码
重复的功能的代码要及时使用函数复用，不要硬编码。
因为在函数逻辑修改的时候，硬编码很容易导致忽略一些函数

### 采用默认参数精简代码
参数的定义和变量的定义善于使用默认值，可以精简变量和减少异常处理

### 使用 Object.assign 设置默认对象
在对象的定义中，学会使用默认对象。在一个对象定以后被调用的时候，不要重复定义传递的对象内容，可以使用默认对象的方法传递对象的内容

```javascript
var menuConfig = {
  title: 'Order',
  // User did not include 'body' key
  buttonText: 'Send',
  cancellable: true
}

function createMenu(config) {
  config = Object.assign({
    title: 'Foo',
    body: 'Bar',
    buttonText: 'Baz',
    cancellable: true
  }, config);

  // config now equals: {title: "Order", body: "Bar", buttonText: "Send", cancellable: true}
  // ...
}

createMenu(menuConfig);
```


### 不要使用标记(Flag)作为函数参数
参数不要使用flag（似乎本来就没用使用过），暂且标注一下
**反例**:
```javascript
function createFile(name, temp) {
  if (temp) {
    fs.create('./temp/' + name);
  } else {
    fs.create(name);
  }
}
```

**正例**:
```javascript
function createTempFile(name) {
  fs.create('./temp/' + name);
}

----------


function createFile(name) {
  fs.create(name);
}
```

### 避免副作用
一个函数的功能要单一，不要以为处理某个事件而修改了全局变量什么的，特别是涉及深复制和浅复制的时候。

修改某个文件的时候要使用唯一的函数，不要很多函数都能修改同一个文件，尽量高内聚，低耦合。

### 不要写全局函数
减少全局函数，不要让某个函数的功能过于强大甚至能够修改全局变量。
否则很容易造成全局污染

使用 ES6 中的 class 对全局的 变量 做继承更好。
```javascript

class SuperArray extends Array {
  constructor(...args) {
    super(...args);
  }
  ...
}

```


### 采用函数式编程
FP模式更痛一理解，比OP更加适合js
函数关联函数，一目了然

### 封装判断条件
判断条件可以封装为一个函数，在函数中判断后进行return true || false；

需要该判断功能的调用该函数

### 避免“否定情况”的判断
尽量少使用否定判断，比如  {!subjects && ...}

### 避免条件判断
能使用三目判断的时候就不要使用if else 、switch等，保证函数功能的单一性。
定义为多态也可以，把他们都继承了。

```javascript
class Airplane {
  //...
}

class Boeing777 extends Airplane {
  //...
  getCruisingAltitude() {
    return getMaxAltitude() - getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  //...
  getCruisingAltitude() {
    return getMaxAltitude();
  }
}

class Cessna extends Airplane {
  //...
  getCruisingAltitude() {
    return getMaxAltitude() - getFuelExpenditure();
  }
}
```

### 避免类型判断
弱类型语言尽量不要使用强类型的定义和需求，不然在toString（） parseInt（）等方面很容易出问题

如果需处理的数据为字符串，整型，数组等类型，无法使用多态并仍有必要对其进行类型检测时，可以考虑使用 TypeScript。

```javascript
function combine(val1, val2) {
  return val1 + val2;
}
```

### 避免过度优化
代码优化上不要过度优化，很多浏览器都具有代码优化功能，过度优化太浪费时间

### 删除无效的代码
无用的代码要及时删除

## **对象和数据结构**
### 使用 getters 和 setters  **（需要继续研究）**
JS 没有接口或类型，因此实现这一模式是很困难的，因为我们并没有类似 `public` 和 `private` 的关键词。

然而，使用 getters 和 setters 获取对象的数据远比直接使用点操作符具有优势。为什么呢？

1. 当需要对获取的对象属性执行额外操作时。
2. 执行 `set` 时可以增加规则对要变量的合法性进行判断。
3. 封装了内部逻辑。
4. 在存取时可以方便的增加日志和错误处理。
5. 继承该类时可以重载默认行为。
6. 从服务器获取数据时可以进行懒加载。


**反例**:
```javascript
class BankAccount {
  constructor() {
	   this.balance = 1000;
  }
}

let bankAccount = new BankAccount();

// Buy shoes...
bankAccount.balance = bankAccount.balance - 100;
```

**正例**:
```javascript
class BankAccount {
  constructor() {
	   this.balance = 1000;
  }

  // It doesn't have to be prefixed with `get` or `set` to be a getter/setter
  withdraw(amount) {
  	if (verifyAmountCanBeDeducted(amount)) {
  	  this.balance -= amount;
  	}
  }
}

let bankAccount = new BankAccount();

// Buy shoes...
bankAccount.withdraw(100);
```

### 让对象拥有私有成员
通过闭包处理一些问题。  **（这岂不是和函数独立性冲突了？）**
答： 不冲突，就是因为闭包让函数有私有成员


## **类**
### 单一职责原则
每个类的职责要单一，比如他是用来处理数据的，比如他是提供渲染的……
不然过高的内聚导致修改时很困难，并且健壮性不强

### 开/闭原则
模块应该已与拓展，不要一次写成后以后无法修改，允许以后拓展功能，比如一些参数单独之类的，或者留些函数接口供以后拓展，调用该函数就能拓展该功能（比如往array添加数据）



### 利斯科夫替代原则
子类对象应该能购替换父类对象

“子类对象应该能够替换其超类对象被使用”。

也就是说，如果有一个父类和一个子类，当采用子类替换父类时不应该产生错误的结果。

### 接口隔离原则
接口要有用处，一个函数或对象或程序不要依赖一些无用或可有可无的接口

### 依赖反转原则
1. 低层模块依赖高层模块，不可翻转（比如删除低层模块后高层模块也能正常使用，不然就尴尬了）。最好的是都依赖接口
2. 抽象接口应该脱离具体实现，具体实现应该依赖于抽象接口。

### 能使用ES6就不用ES5
因为ES5的function在继承，构造和创建模块等方面读取性差。

特别是使用继承的时候

但是，当在需要更大更复杂的对象时，最好优先选择更小的 function 而非 classes。

### 使用方法链
函数的方法链使用 ：let car = new Car().setColor('pink').setMake('Ford').setModel('F-150').save();

### 优先使用组合模式而非继承
能不用继承的时候就不用继承（要开始学习一下设计模式）

除非：（有点难懂）
1. 继承关系表现为"是一个"而非"有一个"(如动物->人 和 用户->用户细节)
2. 可以复用基类的代码("Human"可以看成是"All animal"的一种)
3. 希望当基类改变时所有派生类都受到影响(如修改"all animals"移动时的卡路里消耗量)

**反例**:
```javascript
class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // ...
}

// Bad because Employees "have" tax data. EmployeeTaxData is not a type of Employee
class EmployeeTaxData extends Employee {
  constructor(ssn, salary) {
    super();
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}
```

**正例**:
```javascript
class Employee {
  constructor(name, email) {
    this.name = name;
    this.email = email;

  }

  setTaxData(ssn, salary) {
    this.taxData = new EmployeeTaxData(ssn, salary);
  }
  // ...
}

class EmployeeTaxData {
  constructor(ssn, salary) {
    this.ssn = ssn;
    this.salary = salary;
  }

  // ...
}
```

## **测试**
### 单一的测试每个概念
每个测试都是单一的，不要即测试这有测试那，类似函数的功能单一性原则

## **并发**
### 用 Promises 替代回调
（nodejs 喜欢使用回调函数）

回调函数容易造成大规模嵌套。ES6 内嵌了 Promises（then方法）解决这种问题。

听说ES7的await方法不错……

### Async/Await 是较 Promises 更好的选择
（await出现了……）

Promises 是较回调而言更好的一种选择，但 ES7 中的 async 和 await 更胜过 Promises。

在能使用 ES7 特性的情况下可以尽量使用他们替代 Promises。


## **错误处理**
错误抛出是个好东西！这使得你能够成功定位运行状态中的程序产生错误的位置。

### 别忘了捕获错误
console有方法有很多，详见note

及时使用try/catch方法处理异常

处理异常要详细有效，不要弄个console.log扔在那里

## **代码格式化**

### 大小写一致
函数定义大小写要一直，重申了函数名定义和变量名定义的重要性。

不要出现同一类函数或变量一个大写一个小写

### 调用函数的函数和被调函数应放在较近的位置
函数创建和被调用位置要相近，不要一个在文件头，一个在文件尾，思君不见君

## **注释**
### 只对存在一定业务逻辑复制性的代码进行注释
不要遗留一些没什么必要性的注释，好的函数和变量就能让人看懂功能

### 不要在代码库中遗留被注释掉的代码
废弃的代码要及时处理掉，需要的话从版本控制中寻找

### 不需要版本更新类型注释
版本更新就是用版本控制工具，不要写在js文件中之类的

### 避免位置标记
使用注释行标记一些位置没有什么意义

### 避免在源文件中写入法律评论
（暂时用不到）
将`LICENSE` 文件置于源码目录树的根目录，单独存放，而不是写在js文件等地方
