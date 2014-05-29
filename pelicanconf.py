#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import random

AUTHOR = u'Jackson Gothe-Snape'
SITENAME = u'jackson.gs'

PROFILE_IMG_URL = 'https://pbs.twimg.com/profile_images/378800000813480994/1487341b80b9053dd39c103a7ca51eef.png'

TIMEZONE = 'Australia/Canberra'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = 'themes/pure-single'
OUTPUT_PATH = 'output/'
PATH = None
PAGE_DIR = 'pages'
COVER_IMG_URL = 'http://jackson.gs/images/stairs.jpg'
tags = ["Nobody's home","Nope unintended","Vanity fare"]
#TAGLINE = random.choice(tags)

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('About', 'pages/about-jackson.html'),)


# Blogroll
#LINKS =  (('About', '/pages/about-jackson.html'),)
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget

SOCIAL =     (('github', 'https://github.com/jacksongs/'),('twitter-square', 'https://twitter.com/jacksongs'),('linkedin', 'https://au.linkedin.com/in/jacksongs'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook','sitemap']

EXTRA_HEADER = open('header.html').read().decode('utf-8')
