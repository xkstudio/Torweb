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
import tornado.locale
import platform
import db
from tornado.log import gen_log
from handler.page import Page404Handler
from config.settings import *
from handler import route
from ui_modules import UIModules


class App(tornado.web.Application):

    def __init__(self,handlers,conf,log):
        self.__version__ = conf['version']
        self.log = log
        settings = conf['app_settings']
        settings['default_handler_class'] = Page404Handler  # 404
        settings['ui_modules'] = UIModules
        tornado.web.Application.__init__(self, handlers, **settings)
        #每10秒执行一次
        #tornado.ioloop.PeriodicCallback(self.test, 1 * 10 * 1000).start()
        #封装数据库
        _c = conf['db']
        self.db = db.DB(_c['host'],_c['port'],_c['user'],_c['pass'],_c['db'],_c['charset'])
        #Redis
        _c = conf['redis']
        R = db.Redis(_c['host'],_c['port'],_c['db'],_c['password'])
        self.redis = R.Connect()
        # Load Locale
        self.__load_locale(settings['default_lang'])


    #def test(self):
    #    self.log.info('Test')

    # Load Locale
    def __load_locale(self,default_lang):
        tornado.locale.load_translations('locale')
        tornado.locale.set_default_locale(default_lang)

class Torweb():

    def __init__(self,processes=4):
        self.__version__ = '0.0.1'
        self.host = config['host']
        self.port = config['port']
        self.urls = route
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
        http_server = tornado.httpserver.HTTPServer(request_callback=App(self.urls,self.config,self.log), xheaders=True)
        http_server.add_sockets(http_sockets)
        tornado.ioloop.IOLoop.instance().start()