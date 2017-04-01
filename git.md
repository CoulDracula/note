# Git 操作

### 从其他分支拿文件

git checkout branchName /filePath
git checkout master /src/test.js

### git commit comment

##### 修 Issue 就写：fixed #OT-183 （注意此句应该在最前面）

##### 小改直接就用一句话说清楚。

##### 大改的，根据 issues 说清楚情况、方案、变化。。。。，

> 如： ‘Change DomStorageEnabled default value to true’ （来自facebook开发者sunnylqm ）


### 取消上次push后的操作：

git checkout .

### 合并远程分支到本地

git fetch origin dev

### 切换到历史版本

git checkout 历史版本号

### 合并某分支到当前分支 （分支合并可以选择任意分支任意版本）

```
git merge <分支名称或id>   (解决分支冲突)
git add .
git commit -m ......
```