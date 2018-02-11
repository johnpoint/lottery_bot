#!/usr/bin/python
# coding:utf-8

import telebot
from telebot import types
import time
import config
import os
import join

TOKEN = os.environ.get('TOKEN') or config.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private':
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, "你好，欢迎使用本机器人\n\n 点击 /help - 获取帮助\n")
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        msg_id = bot.send_message(message.chat.id, "你好，欢迎使用本机器人\n\n 点击 /help - 获取帮助\n").message_id
		time.sleep(5)
        bot.delete_message(message.chat.id,msg_id)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    if message.chat.type == 'private':
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, "/join - 加入抽奖\n/list - 查看名单\n/lottery - 抽奖[admin]\n/clear - 清空名单[admin]\n")
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        msg_id = bot.send_message(message.chat.id, "/join - 加入抽奖\n/list - 查看名单\n/lottery - 抽奖[admin]\n/clear - 清空名单[admin]\n").message_id
		time.sleep(5)
        bot.delete_message(message.chat.id,msg_id)

@bot.message_handler(commands=['join'])
def send_join(message):
    if message.chat.type == 'private':
        un = message.from_user.username
        code, r = join.add_in(un)
        if code == '1':
            bot.reply_to(message,r)
        else:
            bot.reply_to(message,r)
    else:
        un = message.from_user.username
        code, r = join.add_in(un)
        if code == '1':
            msg_id = bot.reply_to(message, r).message_id
        else:
            msg_id = bot.reply_to(message, r).message_id
		time.sleep(5)
        bot.delete_message(message.chat.id,msg_id)

@bot.message_handler(commands=['list'])
def send_list(message):
    if message.chat.type == 'private' :
        bot.send_chat_action(message.chat.id, 'typing')
        r = join.read_list()
        num = len(open('slist','rU').readlines())
        rr = u'%s \n\n 目前共有%s人参与抽奖哦'%(r,num)
        bot.reply_to(message,rr)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('戳这里！', url = 'https://t.me/yahahaabot')
        markup.add(btn)
        msg_id = bot.send_message(chat_id=message.chat.id, text=u'为了防止刷屏，请在私聊中使用此命令哦～',reply_markup=markup).message_id
		time.sleep(5)
        bot.delete_message(message.chat.id,msg_id)


@bot.message_handler(commands=['lottery'])
def send_welcome(message):
    un = message.from_user.username
    f = open('adminlist', 'r')
    l = f.read()
    if message.chat.type == 'private':
        if l.find('%s' %un) == -1:
            bot.reply_to(message,'您没有权限哦')
        else:
            code, r = join.get_lottery()
            bot.reply_to(message,r)
    else:
        if l.find('%s' %un) == -1:
            msg_id = bot.reply_to(message,'您没有权限哦').message_id
			time.sleep(5)
            bot.delete_message(message.chat.id,msg_id)
        else:
            code, r = join.get_lottery()
            bot.reply_to(message,r)

@bot.message_handler(commands=['clear'])
def send_welcome(message):
    un = message.from_user.username
    f = open('adminlist', 'r')
    l = f.read()
    if message.chat.type == 'private':
        if l.find('%s' %un) == -1:
            bot.reply_to(message,'您没有权限哦')
        else:
            r = join.del_list()
            bot.reply_to(message,r)
    else:
        if l.find('%s' %un) == -1:
            msg_id = bot.reply_to(message,'您没有权限哦').message_id
			time.sleep(5)
            bot.delete_message(message.chat.id,msg_id)
        else:
            r = join.del_list()
            msg_id = bot.reply_to(message,r).message_id
			time.sleep(5)
            bot.delete_message(message.chat.id,msg_id)

bot.polling()

