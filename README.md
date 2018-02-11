# lottery_bot # [![Build Status](https://travis-ci.org/johnpoint/lottery_bot.svg?branch=master)](https://travis-ci.org/johnpoint/lottery_bot)

## 简介 ##

一个用于抽奖的telegrambot

命令

```
help - 帮助
join - 参与抽奖
list - 显示参与名单
clear - 清空名单[admin]
lottery - 开奖！[admin]
```

## 使用 ##

```
git clone https://github.com/johnpoint/lottery_bot.git
cd lottery_bot && cd bot
```

把username填入adminlist文件中，即为bot管理员**一行一个username**

token填入config.py中

```
pip install pytelegramapi
python main.py
```

**python 2.7测试通过，python3可能会出现奇奇怪怪的问题哦～**

## LICENSE ##

[GNU General Public License v3.0](https://github.com/johnpoint/lottery_bot/blob/master/LICENSE)
