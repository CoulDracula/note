# 开发规范

## 敏捷开发

### 功能实现

- 根据原型设计和需求分析创建相关task
- 在webstorm中选择task创建相关git分支
- 在该分之下完成代码
- 首次commit 后在upsource后创建review
- 每次commit 描述相关问题等 ZS_NB-33
- 等待review
- 无误后合并分支到相关主分支
- 关闭task

### bug处理

1. 出现bug后创建bug issues ，设置为相关task的子任务 ，详细描述该bug
1. 在相关分支修复bug
1. 修复完成后commit
1. 关闭bug issues

*********

## 英文注释

- issues 问题
- dashboard 控制面板
- agile boards 敏捷板
- reports 报告
- projects 项目
- commit 提交
- command 命令

### state

- submitted 提交
- open  开启中
- in progress 进行中
- to be discussed 要讨论的
- reopened 重新打开
- can't reproduce  无法重开
- duplicate 重复
- fixed 修复
- won't fixed 未修复
- incomplete 不完整
- obsolete 已过时
- verified 已验证
- overdue 逾期
- wait for reproduce 等待重开
- approved 提准

### type

- bug 错误
- cosmetics 原型
- exception 特例
- feature 特征
- task 任务
- usability problem 可用性问题
- performance problem 性能问题
- epic 巨作

- project 项目
- priority 优先级
- assignee 受让人
- fix versions 修复版本
- unscheduled 固定

********

## 开发流程

1. 开始做
1. In Progress Fixed
  - Bug已修复 Won't Fix
  - 不修复 Verified
  - Task验证无误