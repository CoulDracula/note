# Node.js

## 常见 Node.js 开发问题

### express 使用 ES 6

#### 如何在 express 中使用 ES 6 语法

**http://www.tuicool.com/articles/Y3u63u6**


### API Guide | restify

**http://restify.com/**

### RESTful api 设计指南

**http://www.ruanyifeng.com/blog/2014/05/restful_api.html**

### 发送邮件

```javascript
  var api_key = 'key-47b43c1161cdf7d1d68b4fa69cf45cb2';
  var domain = 'sandbox0f3e7462e8ba4274a83d05a363f1e63f.mailgun.org';
  var mailgun = require('mailgun-js')({ apiKey: api_key, domain: domain });


  var data = {
    from: 'Excited User <postmaster@sandbox0f3e7462e8ba4274a83d05a363f1e63f.mailgun.org>',
    to: 'coulturing@gmail.com',
    subject: 'Hello',
    text: 'Testing some Mailgun awesomness!'
  };
  mailgun.messages().send(data, function (error, body) {
      if (!error) {
        res.send({ title: 'succ' });
        console.log(body);
      }
      else {
        res.send({ title: 'err' });
      }
    }
  );
```

### forever

forever 执行 `npm start`

https://github.com/foreverjs/forever/issues/540

- 执行指定位置的：
`forever start -c "npm start" /path/to/app/dir/`

- 执行当前位置的：
`forever start -c "npm start" ./`