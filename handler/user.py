#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler

class LoginHandler(BaseHandler):

    def get(self):
        self.render('user/login.html')

class RegisterHandler(BaseHandler):

    def get(self):
        self.render('user/register.html')