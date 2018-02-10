#!/usr/bin/python
# encoding=utf-8

import linecache
import random
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def add_in(user):
    f = open('list', 'r')
    l = f.read()
    if l.find('%s' %user) == -1:
        f = open('list', 'a+w')
        r = user
        print >> f, r
        f.close()
        sf = open('slist','a+w')
        s = ' | '
        localtime = time.strftime("%H:%M:%S", time.localtime())
        rr = localtime + s + r
        print >> sf,rr
        sf.close()
        return 1, '成功参加抽奖~'
    else:
        return 0, '你已经参加了哦~耐心等待开奖吧！'

def get_lottery():
    count = len(open('list', 'r').readlines())
    if count == '0':
        return 0,'None'
    else:
        with open('list') as f:
            l = f.read().splitlines()
            r = random.sample(l,1)
            a = ''.join(r)
            rr = u'我抽中了： @%s'%a
    return 1,rr

def read_list():
    f = open('slist')
    r = f.read()
    f.close()
    return r

def del_list():
    f = open('list', 'w')
    f.close()
    sf = open('slist','w')
    sf.close()
    return '名单已清空~'
