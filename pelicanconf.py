#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import math

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
PLUGINS = ['i18n_subsites', 'code_directive']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'fr'

# Theme
THEME = "themes/hpc_math_theme"

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

MENUITEMS = [('Présentation', '/index.html'),
             ('Codes', '/pages/codes.html'),
             ('Enseignement', '/pages/enseignement.html'),
             ('Partenaires', '/pages/partenaires.html'),
             ('Recherche', '/pages/recherche.html'),
             ("Ressources", '/pages/ressources.html'),
]

# LOGOS = os.listdir('content/images/logo')
# LOGOS.sort()
# LOGOS_NCOLS = 3
# LOGOS_NROWS = math.ceil(len(LOGOS)/LOGOS_NCOLS)
# print(len(LOGOS))
# print(LOGOS)