# Torweb

Advanced web application based on Tornado.


### Features

- [x] Non-blocking Network I/O

- [x] Session Support (Use Redis Storage)

- [x] Cookie(Secure Cookie) Support

- [x] MySQL Support

- [x] Redis Support


### Torweb Version

> **v0.0.1**


### Python Support

- [x] Python 2.6.6

- [x] Python 2.7.x

- [ ] Python 3.x Not Test


### Web Framework

* Tornado 4.4.3


### Front Framework

* Bootstrap 3.3.7

* Font-Awesome 4.7.0

* jQuery 2.2.4


### Database Support

* [MySQLdb](https://pypi.python.org/pypi/MySQL-python) 1.2.5

* [Redis](https://pypi.python.org/pypi/redis) 2.10.5


### Installation

* yum install MySQL-python

* pip install tornado

* pip install redis


### Startup

> python run.py

You can visit the site via http://YourIP:8888/

Specify Listen Port:

> python run.py --port=8080


### Development

* Configuration

config/settings.py

> You can config your MySQL and Redis via settings.py.

* Handlers

handler/YourHandler.py

> Add **import YourHandler** to handler/__init__.py and add don't forget to add a route.

* Templates

view/{Handler}/{Template}.html