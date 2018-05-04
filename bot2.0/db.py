#!/usr/bin/python3

import sqlite3

def new_po(poid):
    db = sqlite3.connect("bot.db")
    cur = db.cursor()
    bna = cur.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
    if bna.find('%s'%poid) ==-1:
        cur.execute("""create table %s ( id integer primary key, name varchar(36) UNIQUE )""")%poid
        return 0
    else:
        return 1
        
def new_user(poid,uid):
    db = sqlite3.connect("user.db")
    cur = db.cursor()
    bna = cur.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
    if bna.find('%s'%poid) ==-1:
        cur.execute("""create table %s ( id integer primary key, name varchar(36) UNIQUE )""")%poid
        return 0
    else:
        return 1