#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jackson Gothe-Snape'
SITENAME = u'jacksongs'
SITEURL = ''
DELETE_OUTPUT_DIRECTORY = False

TIMEZONE = 'Australia/Canberra'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'themes/pure-single'
OUTPUT_PATH = 'output'
PATH = 'content'
COVER_IMG_URL = 'http://37.media.tumblr.com/3f5e020616067de43babe239328274a2/tumblr_mvy15aFi9v1rt9kxoo1_500.gif'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-33090301-1'
DISQUS_SITENAME = 'jacksongs'
