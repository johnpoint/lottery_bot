#!/usr/bin/python3

import telebot
from telebot import types
import time
import config
import os
import join
import getid
import web
import db

TOKEN = config.TOKEN
botname = config.name
bot = telebot.TeleBot(TOKEN)

#36位uuid

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
    if ' ' not in message.text :
        bot.reply_to(message, '没有识别到有效的口令…')
    else:
        uid = message.from_user.id
        key = message.text.split(' ')[1]
        dbcode = db.join(uid,key)
        if dbcode == 0:
            bot.send_message(message.chat.id,'已成功加入抽奖')
        elif dbcode == 1:
            bot.send_message(message.chat.id,'此次操作不成功，可能已经加入抽奖')
        else:
            bot.send_message(message.chat.id,'未知错误')


@bot.message_handler(commands=['roll'])
def send_welcome(message):

@bot.message_handler(commands=['new'])
def new_post(message):
    pid = getid.getuuid()
    uid = message.from_user.id
    dbcode = db.new_user(pid,uid)
    if dbcode == 0:
        dbcode = db.new_po(pid)
        if dbcode == 0:
            bot.send_message(message.chat.id,u'新的抽奖已经准备就绪，抽奖口令：\n`%s`'%pid,parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id,'遇见错误，抽奖未能成功创建',parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id,'遇见错误，抽奖未能成功创建',parse_mode='Markdown')

@bot.message_handler(commands=['del'])
def new_post(message):

bot.polling()

