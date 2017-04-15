#!/usr/bin/python
# -*- coding:utf-8 -*-
# Powered By KK Studio

from BaseHandler import BaseHandler

class LoginHandler(BaseHandler):

    def get(self):
        self.render('user/login.html')

    def post(self):
        pass

    def create_session(self,data,remember,cookie_name):
        sid = self.session.gen_session_id()
        self.session.data = data
        self.session.isGuest = False
        #self.session.save() # Why don't save? See self._on_finish !!
        if remember == "yes":
            expires_days = 15  # Remember Session 15 days
        else:
            expires_days = None
        self.set_secure_cookie(cookie_name, sid, expires_days)

class RegisterHandler(BaseHandler):

    def get(self):
        self.render('user/register.html')