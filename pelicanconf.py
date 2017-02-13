#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Dr. D'
SITEURL = 'http://dsict.localhost'
AUTHOR = 'Daniel Schreij'

# Decompose e-mail address so it can be obfusciated later to confuse spambots.
EMAIL_NAME = 'dschreij'
EMAIL_DOMAIN = 'gmail'
EMAIL_EXT = 'com'

GITHUB_URL = "http://github.com/dschreij/"
GITHUB_USER = "dschreij"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = "true"

WELCOME_MESSAGE = (
	'Welcome to my little space on the web where I express my thoughts about '
	'software development, psychology, and everything else that keeps me busy.'
)

PROJECTS_INTRO = (
	'This is an overview of projects that I am currently working on, or have '
	'worked on in the past. Some I started by myself to learn the '
	'ropes of the a language/framework/toolkit, others were on assignment.'
)

PATH = 'content'
ARTICLE_PATHS = ['blog','projects']

TIMEZONE = 'Europe/Amsterdam'

DIRECT_TEMPLATES = ['index', 'archives', 'categories', 'authors', 'tags']
DISPLAY_CATEGORIES_ON_MENU = False

# Tell Pelican to add 'images' and 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'css/custom.css']

# Tell Pelican to change the path to 'theme/css/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'css/custom.css': {'path': 'theme/css/custom.css'}
}

PLUGIN_PATHS = ['plugins',]
PLUGINS = ['standalone_categories', 'tag_cloud']

STANDALONE_CATEGORY_PAGES = [
    {
        'category_name': 'Projects', 
        'page_template': 'projects',
        'article_template': 'project_article'
    },
]

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'menu-order'
TAGS_URL = 'tags.html'
CATEGORIES_URL = 'categories.html'

EXTRA_TEMPLATES_PATHS = ['custom_templates']
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
	('Blog', '/index.html'),
	('Projects','/projects.html'),
	('Bio','/bio.html')
]

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
	('linkedin', 'http://www.linkedin.com/in/dschreij'),
	('github', GITHUB_URL),
	('stackoverflow', 'http://stackexchange.com/users/1582305/daniel-s', 'stack-overflow'),
	('OSF', 'https://osf.io/gj72y/', 'share-alt'),
)

DEFAULT_PAGINATION = False
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = True
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme settings
THEME = 'themes/pelican-bootstrap3'
CUSTOM_CSS = 'theme/css/custom.css'
BOOTSTRAP_NAVBAR_INVERSE = True
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'
BANNER = 'images/HeaderWeb.png'

ABOUT_ME = None
CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS_UNIVERSAL = "UA-71223842-3"
# DISQUS_SITENAME = "dsitforscience"
# DISQUS_DISPLAY_COUNTS = False


