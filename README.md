# lottery_bot  [![Build Status](https://travis-ci.org/johnpoint/lottery_bot.svg?branch=master)](https://travis-ci.org/johnpoint/lottery_bot) [![GitHub version](https://badge.fury.io/gh/johnpoint%2Flottery_bot.svg)](https://badge.fury.io/gh/johnpoint%2Flottery_bot)

# 简介 #

一个用于抽奖的telegram bot

# 命令

```
help - 帮助
join - 参与抽奖
list - 显示参与名单
clear - 清空名单[admin]
lottery - 开奖！[admin]
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

# LICENSE #

[GNU General Public License v3.0](https://github.com/johnpoint/lottery_bot/blob/master/LICENSE)
