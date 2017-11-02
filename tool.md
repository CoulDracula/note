## Tool
### docker
- 当镜像运行成功后，会自动创建一个有独立名称、网络的容器。
- 同一个仓库里可以有多个相同名称镜像，通过tag标签区分
- 创建步骤：先创建基础镜像，做成容器，在其中添加相关代码运行环境（如：nodejs，mongodb），将其创建为新容器，该容器创建为镜像。在镜像中添加程序文件（如：webapp文件夹）。运行
- (原始镜像没有vim，无法访问外网，可以用cat命令创建hosts，合并到现有hosts)


#### 构建parse服务器+docker数据库流程代码
```dockerfile
docker pull mongo
docker run  --name parse-database   -p 27017:27017   -d mongo

parse-server --appId 1 --masterKey 1 --databaseURI mongodb://localhost:27017/parse-database

 parse-dashboard --appId 1 --masterKey 1  --serverURL "http://localhost:1337/parse" --appName parse-database

```




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



