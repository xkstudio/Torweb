#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import MySQLdb

class DB:

    def __init__(self,host,port,user,passwd,dbname,charset="utf8"):
        self._conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset=charset)
        self._cur = self._conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def __del__(self):
        self.close()

    def close(self):
        self._cur.close()
        self._conn.close()

    def select(self,sql):
        self._cur.execute(sql)
        return self._cur.fetchall()

    def get(self,sql):
        self._cur.execute(sql)
        return self._cur.fetchone()

    def update(self,sql):
        pass

    def delete(self,sql):
        pass

    def insert(self,sql):
        pass