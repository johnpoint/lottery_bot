# lottery_bot  [![Build Status](https://travis-ci.org/johnpoint/lottery_bot.svg?branch=master)](https://travis-ci.org/johnpoint/lottery_bot) [![GitHub version](https://badge.fury.io/gh/johnpoint%2Flottery_bot.svg)](https://badge.fury.io/gh/johnpoint%2Flottery_bot)

# 声明 #

# 简介 #

一个用于抽奖的telegram bot

# 命令

## bot1.0

```
help - 帮助
join - 参与抽奖
list - 显示参与名单
clear - 清空名单[admin]
lottery - 开奖！[admin]
```

## bot2.0

*开发未完成*

```
new -新建一个抽奖（会生成唯一uuid）
close - 关闭一个抽奖（后跟唯一uuid）
del - 删除一个抽奖（后跟唯一uuid）
join - 参与抽奖（后跟唯一uuid）
list - 显示参与名单（后跟唯一uuid）
roll - 开奖！（后跟唯一uuid）
help - 帮助
```

# 部署 #

```
git clone https://github.com/johnpoint/lottery_bot.git
cd lottery_bot
pip install -r requirements.txt
cd bot
```

## 设置BOT管理员 ##

username填入adminlist文件中，即为bot管理员

**一行一个username**

token填入config.py
bot的username也填入config.py

```
python main.py
```

# TODO #

- [ ] 显示设置username帮助
- [ ] 自动备份名单
- [ ] 防误删处理
- [ ] 绑定群组

**python 2.7测试通过，python3可能会出现奇奇怪怪的问题哦～**

# LICENSE #

[GNU General Public License v3.0](https://github.com/johnpoint/lottery_bot/blob/master/LICENSE)
