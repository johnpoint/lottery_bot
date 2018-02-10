#!/usr/bin/python
# coding:utf-8

import telebot
import config
import os
import join

TOKEN = os.environ.get('TOKEN') or config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "你好，欢迎使用本机器人\n\n 点击 /help - 获取帮助\n")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "/join - 加入抽奖\n/list - 查看名单\n/lottery - 抽奖[admin]\n/clear - 清空名单[admin]\n")

@bot.message_handler(commands=['join'])
def send_join(message):
    un = message.from_user.username
    code, r = join.add_in(un)
    if code == '1':
        bot.reply_to(message,r)
    else:
        bot.reply_to(message,r)

@bot.message_handler(commands=['list'])
def send_list(message):
    r = join.read_list()
    num = len(open('slist','r').readlines())
    rr = u'%s \n\n 目前有%s个用户参与抽奖！'%(r,num)
    bot.reply_to(message,rr)

@bot.message_handler(commands=['lottery'])
def send_welcome(message):
    un = message.from_user.username
    f = open('adminlist', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'您没有权限哦')
    else:
        code, r = join.get_lottery()
        bot.reply_to(message,r)

@bot.message_handler(commands=['clear'])
def send_welcome(message):
    un = message.from_user.username
    f = open('adminlist', 'r')
    l = f.read()
    if l.find('%s' %un) == -1:
        bot.reply_to(message,'您没有权限哦')
    else:
        r = join.del_list()
        bot.reply_to(message,r)

bot.polling()
