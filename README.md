Torweb
=========

Advanced web application based on Tornado.


## Version

**v1.0.6-Beta**


## Features

- [x] Non-blocking Network I/O

- [x] Session Support (Use Redis Storage)

- [x] Cookie(Secure Cookie) Support

- [x] MySQL Support

- [x] Redis Support

- [x] Jinja2 Support

- [x] Internationalization Support (i18n)


## Python Support

- [x] Python 2.6.6

- [x] Python 2.7.x

- [ ] Python 3.x Not Test


## Web Framework

* [Tornado](http://www.tornadoweb.org) 4.0+


## Front Framework

* Bootstrap 3.3.7 (Not Limit)

* Font-Awesome 4.7.0 (Not Limit)

* jQuery 2.2.4 (Not Limit)


## Template Egnine

* [Jinja2](http://jinja.pocoo.org/) 2.9+


## Database Support

* [MySQLdb](https://pypi.python.org/pypi/MySQL-python) 1.2.5

* [Redis](https://pypi.python.org/pypi/redis) 2.10.5


## Installation

* yum install MySQL-python

* pip install tornado

* pip install redis

* pip install jinja2


## Startup

> python run.py

You can visit the site via http://YourIP:8081/

Specify Port:

> python run.py --port=8080


## Development

#### Configuration

* config/settings.py

> You can config your MySQL and Redis via settings.py.

#### Handlers

* handler/__init__.py

* handler/YourHandler.py

> Add **import YourHandler** to handler/__init__.py and add don't forget to add a route.

#### Templates

* view/YourHandler/YourTemplate.html

> Support for **Jinja2**, you should do this:

```python
from Template import TemplateLoader
tpl_loader = TemplateLoader(settings['template_path'], False)
tornado.web.Application.__init__(self, handlers, template_loader=tpl_loader.Loader(), **settings)
```

> See the app/Torweb.py for the detail.


#### Static Files

* static/css

* static/js

* static/img

#### UI Modules

* ui_modules/UIModules.py

* view/ui_modules/YourUIModule.html

> Via **{{ module YourUIModule(foo) }}** use ui modules in template.

Tips: **Jinja2 don't support UI Modules**

#### Internationalization

* locale/en_US.csv

* locale/YourLocale.csv

> Via **{{ _('Locale String') }}** in your template


## License

This project is under the MIT License. See the [LICENSE](https://github.com/kkstu/Torweb/blob/master/LICENSE) file for the full license text.
