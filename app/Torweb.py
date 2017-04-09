#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process
import tornado.options
import platform
from Log import Log
from db import Redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from handler.page import Page404Handler

from config.settings import settings as Settings
from config.settings import config as Config
from handler import route


class App(tornado.web.Application):

    def __init__(self,handlers,settings,conf):
        settings['default_handler_class'] = Page404Handler # 404
        tornado.web.Application.__init__(self, handlers, **settings)
        #后台日志高亮输出
        tornado.options.parse_command_line()
        #每10秒执行一次
        #tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()
        self.__version__ = conf['version']
        #封装数据库
        self._db = conf['db']
        db_engine = create_engine(self.__gen_db_conn(),encoding='utf-8', echo=False)
        self.db = scoped_session(sessionmaker(bind=db_engine))
        #Redis
        _redis = conf['redis']
        R = Redis(_redis['host'],_redis['port'],_redis['db'],_redis['password'])
        self.redis = R.Connect()

    def __gen_db_conn(self):
        conn = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=%s' % \
            (self._db['user'], self._db['pass'], self._db['host'], self._db['port'], self._db['db'], self._db['charset'])
        return conn

    #def test(self):
    #    print "Test"

class Torweb():

    def __init__(self,host,port,processes=4):
        self.__version__ = '0.0.1'
        _log = Log()
        self.log = _log.info
        self.host = host
        self.port = port
        self.urls = route
        self.settings = Settings
        self.config = Config
        self.config['version'] = self.__version__
        if platform.system() == "Linux":  #根据操作系统类型来确定是否启用多线程
            self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次
        else:
            self.processes = 1

    #多线程模式
    def run(self):
        self.log('Torweb %s' % self.__version__) # 启动时打印版本号
        self.log('Listen Port: %s' % self.port)
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=App(self.urls,self.settings,self.config), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()