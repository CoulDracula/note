## Language
### mongodb

- `mongod -dbpath "g:\net+\nodejs\redux_test\database"`
- `use test`
- `db.redux_test_database.find()`


### nodejs
- express
  - express 无法直接快速创建express服务器
  - npm install express-generator
  - express ${demo name}


### JavaScript 语法标准

- 封装模块为方法
```
String.method("deentityify",function(){  //封装string类型的方法
    var entity={
        quot:'"',
        lt:'<',
        gt:'>'
    };
    return function () {        //返回deentityify方法
        return this.replace(/&([^&;]+)/g,
            function(a,b){
                var r= entity[b];
                return typeof r=== 'string'?r:a;
            }
        );
    };

}());       //此处‘（）’为了当使用deentityify方法时立即调用
```
- 封装函数为模块（）
```
var serial_marker=function(){
    var prefix="";	//私有变量
    var seq=0;		//私有变量
    return {
        set_prefix:function(p){
            prefix=String(p);
        },
        set_seq:function(s){
            seq=s;
        },
        gensym:function () {
            var result=prefix+seq;
            return result;
        }
    }
};
//模块调用
var seqer=serial_marker();
seqer.set_prefix("q");
seqer.set_seq(1000);
var test=seqer.gensym();    //test='q1000'
```

- 科里化（将函数和其传的参数构造成一个新函数，一般用于处理多个参数的函数）
```

```
- 函数记忆（用来解决同一个函数相同参数的多次计算）

	方法：创建一个新函数（也可以用原始函数），新函数中包含数组，用来存储需要重复计算的数值

	例如Fibonacci数列（原始函数添加数组）
```
//创建一个例如memo的数组保存每次调用的结果
//数组初始化为nemo[0,1]
var Fibonacci =function () {
    var memo=[0,1];
    var fib=function (n) {
        var result=memo[n];
        if(typeof result!=='number'){
            result =fib(n-1)+fib(n-2);
            memo[n]=result;
        }
        return result;

    };
    return fib;
}();
```
- 函数调用方法：

1、函数调用：
```
var ass =function (num) {
    var numA=num;
    numA+=10;
    return{
    numA}
};
var a=ass(2);
```

2、构造器调用：
```
var quo=function(string){
	this.status=string;
};
quo.prototype.get_status=function(){
	return this.status;
};
var myQuo=new quo("ahahaha");
document.write(myQuo.get_status());  //ahahaha

```

3、方法调用：
```
var myObject ={
    value:0,
increment:function(inc){
    this.value+=typeof inc === 'number'?inc:1;

}
};
myObject.increment(2);
document.write(myObject.value);
```
(createClass创建组建就是创建了一个方法)

### array方法
- array.concat(item...)

		a.conca(b);	// 将b中的内容添加到a数组末尾
- array.push(item...)

		a.push(b)  //同上
- array.sort(comparefn)   //排序
- array.slice(start,end);  //复制从下标为start的开始，下标为end的

		var b=a.slice(0,1);
- array.reverse();		//逆序排列
- array.shift();	//移除首个元素（队列）
- array.pop();	//移除末尾元素并返回末尾元素（栈）

### number
- number.tuString(radix);	//转为字符串,radix:进制数
- number.toPrecision(precision);	//转为十进制的字符串，presion：精度
- number.toFixed(fractionDigits);	//同上

### string
- string.charAt(pos);	//返回pos位置的字符
- string.concat(string);	//类似array.concat()，合并 （很少使用）
- string.indexOf(sreachString,position);	//查找sreachString位置。position为返回的该位置，找不到返回-1
- string.sreach(regexp);	//类似indexOf，不过他是匹配正则表达式



## Notes&Code model
- 在es6中自己创建函数尽量不要使用function(){}，而是用()=>{}。因为箭头函数省掉了var this=this、.bind(this)
- 使用class xxx extends React.Component{}构造组建，一定记得定义数据类型
```
constructor(props) {
  super(props);
}
```
```
PersonalDataForm.PropTypes={
  personalData: React.PropTypes.string,
  text: React.PropTypes.string,
  FormData:React.PropTypes.array
};
```
- 使用const xxx =React.createClass({});就不用定义了，需要的时候再定义
有多个数据类型组成的json格式的数据的格式是object。



### 关于jquery ajax方法上传数据，nodejs显示数据类型未知

将bodyParser中间件用来解析http请求体的部分放在路由配置之前
bodyParser.json是用来解析json数据格式的。
bodyParser.urlencoded则是用来解析我们通常的form表单提交的数据，也就是请求头中包含这样的信息： Content-Type: application/x-www-form-urlencoded

bodyParser.urlencoded
模块用于解析req.body的数据，解析成功后覆盖原来的req.body，如果解析失败则为 {}
```
const bodyParser =require("body-parser");
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
（bodyParser要在express路由之前，）
```
