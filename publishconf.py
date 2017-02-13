#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://dschreij.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

LOAD_CONTENT_CACHE = True

GITHUB_URL = "http://github.com/dschreij/"
GITHUB_USER = "dschreij"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = "true"

DISQUS_SITENAME = "dsitforscience"
DISQUS_DISPLAY_COUNTS = True
# GOOGLE_ANALYTICS = ""
GOOGLE_ANALYTICS_UNIVERSAL = "UA-71223842-3"
