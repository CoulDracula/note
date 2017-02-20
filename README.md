# note
study note

## [更简洁的 JavaScript 风格](clean-code-js# 更简洁的 JavaScript 风格)

## 零碎笔记
- 收到新数据后`componentWillReceiveProps:function(nextProps){...nextProps}`
- 挂载前`componentWillMount:function(){...可以是state}`
- 挂载后`componentDitMount:function(){...可以是state}`
- 是否更新（true更新）`shouldComponentUpdate:function(nextProps,nextState){
  return true/false;
}`
- 更新dom之前,这时候state等不可以改变`componentWillUpdate:function(nextProps,nextState){...}`
- 更新dom之后 `componentDitUpdate:function(prevProps，pervState){...}`
- 卸载元素时 componentWillUnmount


- es6箭头函数省掉了.bind(this)。使用的时候要注意：
```
true:
setTimeout(function(){}.bind(this),time);

false:
setTimeout(function(){},time).bind(this);
```



- 高德地图key：22f193fcd6f2cda7027e7ddd96261a62
- 谷歌地图key：AIzaSyDwlx_b8vggb1Lfx0IyTz1-_eyh6hN5QMQ




# Think&note
## Tool
### docker
- 当镜像运行成功后，会自动创建一个有独立名称、网络的容器。
- 同一个仓库里可以有多个相同名称镜像，通过tag标签区分
- 创建步骤：先创建基础镜像，做成容器，在其中添加相关代码运行环境（如：nodejs，mongodb），将其创建为新容器，该容器创建为镜像。在镜像中添加程序文件（如：webapp文件夹）。运行
- (原始镜像没有vim，无法访问外网，可以用cat命令创建hosts，合并到现有hosts)

方法：

（containername：容器名，imagename：镜像名，filepath：文件位置）

- 要求系统版本3.10以上（`uname -r`查看）
- 安装：`yum -y install curl`  ` curl -sSL https://get.docker.com/ |sh`
- 启动：`systemctl start docker`
- 创建容器：`docker run --name dockername -i -t XXX`(-i:stdin是开启的，-t：分配一个tty伪终端)dockername是自己定义的容器名
- 重启容器：`docker start dockername`
- 进入容器：`docker attach containername`
- 删除容器：`docker rm containername/dockerid`
- 查看容器：`docker ps -a`
- 查看端口号:`docker port containername containerport`(containerport 为端口号)
- 查看容器端口映射：`docker ps -l`
- 查看容器运行日志： `docker logs containername`
- 查看镜像：`docker images`
- 删除镜像：`docker rmi imagename/imageid`
- 下载镜像：`docker pull imagename`
- 修改镜像名：`docker tag oldId newname：newtag`（oldId：源镜像id newname必须为小写）
- 创建容器并写入文件：` docker run -it -v filepath:/host -p 9000:3000 dockerimage /bin/bash`( 9000：3000宿主端口：容器端口)
- 后台运行：`docker run --name contaimername -d -w /microservice -p 9000:3000 dockerimage npm start`(/microservice：要运行的文件夹 -d：分离式后台运行 此为样例，具体内容具体改变)
- 创建新镜像：`docker commit containername newImage`(newImage为新创建的镜像名)

	（如果commit后文件未修改，可以尝试换个终端尝试）

- docker镜像位置： /var/lib/docker/aufs/diff/
- build创建镜像（推荐）：创建Dockerfile
```
		# example
		FROM dockerimage
		MAINTAINER 	author
		ONBUILD filepath # 要添加的文件地址
		RUN apt-get update
		RUN apt-get install node
		RUN apt-get install npm
		EXPOSE 80

	docker build -t="filepath".
		(经验看来docker build . 最好用)
 		(注意build后边的".",)
```
-  关于无法以普通用户身份运行docker
  - docker和当前用户不在同一组
  - groupadd  docker （创建docker组）
  - gpasswd -s ${user} docker
  - restart docker

- Cannot connect to the Docker daemon. Is the docker daemon running on this host?
 docker权限不足，未开启docker或则需要root权限


参考视频：https://www.youtube.com/watch?v=PJ95WY2DqXo
https://www.youtube.com/watch?v=lss2rZ3Ppuk



### JWT (JSON web tokens)
- 安装： npm install jwt-simple --save
- 调用
```
	var jwt = require('jwt-simple');
 	app.set('jwtTokenSecret', 'YOUR_SECRET_STRING');
	（YOUR_SECRET_STRING：jwtTokenSecret）
```

- 生成token
```
var expires = moment().add('days', 7).valueOf();
var token = jwt.encode({
  iss: user.id,
  exp: expires
}, app.get('jwtTokenSecret'));

res.json({
  token : token,
  expires: expires,
  user: user.toJSON()
});
（"days",7   :    token有效期）
```
- jwt.encode()函数有2个参数。第一个就是一个需要加密的对象，第二个是一个加密的密钥

- jwt.sign(payload, secretOrPrivateKey, options, [callback])
```
const jwt = require('jsonwebtoken');
const user={...};

const token = jwt.sign(user, 'shhhhh');

const cert = fs.readFileSync('private.key');
const token = jwt.sign(user, cert, { algorithm: 'RS256'});

```



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


### JavaScript
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
