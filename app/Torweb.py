#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.netutil
import tornado.process
import platform
import tornado.options
from tornado.log import gen_log
from db import DB
from db import Redis
from handler.page import Page404Handler
from config.settings import *
from handler import route


class App(tornado.web.Application):

    def __init__(self,handlers,settings,conf,log):
        self.__version__ = conf['version']
        self.log = log
        settings['default_handler_class'] = Page404Handler  # 404
        tornado.web.Application.__init__(self, handlers, **settings)
        #每10秒执行一次
        #tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()
        #封装数据库
        _db = conf['db']
        self.db = DB(_db['host'],_db['port'],_db['user'],_db['pass'],_db['db'],_db['charset'])
        #Redis
        _redis = conf['redis']
        R = Redis(_redis['host'],_redis['port'],_redis['db'],_redis['password'])
        self.redis = R.Connect()

    #def test(self):
    #    print "Test"

class Torweb():

    def __init__(self,processes=4):
        self.__version__ = '0.0.1'
        self.host = config['host']
        self.port = config['port']
        self.urls = route
        self.settings = config['app_settings']
        self.config = config
        self.config['version'] = self.__version__
        self.log = gen_log
        if platform.system() == "Linux":  #根据操作系统类型来确定是否启用多线程
            self.processes = processes # 当processes>1时，PeriodicCallback定时任务会响相应的执行多次
        else:
            self.processes = 1

    #多线程模式
    def run(self):
        self.log.info('Torweb %s' % self.__version__)  # 启动时打印版本号
        self.log.info('Listen Port: %s' % self.port)
        http_sockets = tornado.netutil.bind_sockets(self.port, self.host)
        tornado.process.fork_processes(num_processes=self.processes)
        http_server = tornado.httpserver.HTTPServer(request_callback=App(self.urls,self.settings,self.config,self.log), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()