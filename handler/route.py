#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio
import index
import page

urls = [
    (r'/',index.IndexHandler),
    (r'/page/404.html',page.Page404Handler),
    (r'/page/blank.html',page.BlankHandler),
]