#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Konsta Kurki'
SITENAME = 'Theoretical Physics Blog'
SITEURL = 'http://localhost:3333'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME="texris"

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 5

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
