#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from glob import glob

AUTHOR = u'Byron J. Smith'
SITENAME = u'Deep Ecology'
SITESUBTITLE = u'A blog of the new microbiology.'
SITEURL = u'http://blog.byronjsmith.com'

# Extract metadata from the filename
FILENAME_METADATA = '(?P<slug>.*)'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Living in an Ivory Basement', 'http://ivory.idyll.org/blog/'),
          ('The Endeavor', 'http://www.johndcook.com/blog/'),
          )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ByronJSmith'),
          ('linkedin', 'https://linkedin.com/profile/view?id=76273001')
          )

#TWITTER_USERNAME = 'byronjsmith'
GITHUB_URL = 'https://github.com/bsmith89'
GITHUB_POSITION = 'right'

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

THEME = 'theme/'
PLUGIN_PATHS = glob("plugins/*/")
PLUGINS=[]

# Cached content is also recompiled.
# Good for testing plugin changes.
LOAD_CONTENT_CACHE = False

MATHJAX = True

SUMMARY_MAX_LENGTH = 150

