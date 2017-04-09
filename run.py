#!/usr/bin/python
# -*- coding:utf8 -*-
# Powered By KK Studio

from app.Torweb import Torweb

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8888
    app = Torweb(host,port)
    app.run()
