# Http

## http 相关问题

### http response 报头

* http://www.runoob.com/http/http-header-fields.html

### http response 和 request  报头

* http://kb.cnblogs.com/page/92320/

### w3相关文档

* https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

### Auth2 token

> OAuth 适合在大型服务器和服务期间用户的身份验证
> JWT适合在自身的登录验证
> apiKey适合开发者的服务器调用其他api的身份验证

Using JSON Web Tokens with Node.js
* https://cnodejs.org/topic/53c652bfc9507b404446ee40


### fetch file

* http://www.tuicool.com/articles/qUBjee7
* 上传文件fetch header 为空，为什么不能有具体的accept值，还不知道

### 关于post 403、400

如果是403 首先检查是不是上传的数据类型错误，比如传了object
如果是400 首先检查是不是上传的字符串关键字不是后台允许的，其次是return fetch的位置是不是能够正常调用

### 服务器端resHeard的设置和接受跨域请求

```javascript
app.all('*', function(req, res, next) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers", "Content-Type,Content-Length, Authorization, Accept,X-Requested-With");
	res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
	res.header("X-Powered-By",' 3.2.1');
	res.header("Content-Type", "application/json;charset=utf-8");
	if(req.method=="OPTIONS")
		res.send(200);/*让options请求快速返回*/
	else  next();
});
```
