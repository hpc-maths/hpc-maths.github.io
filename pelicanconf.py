#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Marc Massot'
SITENAME = 'HPC@Maths'
SITEURL = '/site'
# SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

OUTPUT_PATH = 'public/'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'fr'

# Theme
THEME = "themes/pelican-bootstrap3"

HIDE_SIDEBAR = True
BANNER = 'images/banner.jpg'
BANNER_ALL_PAGES = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
