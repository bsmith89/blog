#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
from privateconf import *

# SITEURL in ./privateconf.py
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/translation/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# DISQUS_SITENAME in ./privateconf.py
# GOOGLE_ANALYTICS in ./privateconf.py
