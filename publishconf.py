#!/usr/bin/env python3
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = "http://blog.byronjsmith.com"
DISQUS_SITENAME = "byronjsmithblog"
GOOGLE_ANALYTICS = "UA-40659359-1"

RELATIVE_URLS = False

# TODO: Do I really want atom feeds?
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# DISQUS_SITENAME in ./privateconf.py
# GOOGLE_ANALYTICS in ./privateconf.py
