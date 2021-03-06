#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

from glob import glob
import os
import sys

sys.path.append(os.curdir)

# Site settings {{{1
AUTHOR = "Byron J. Smith"
SITENAME = "Deep Ecology"
SITESUBTITLE = "A blog of the new microbiology."
SITEURL = "//blog.byronjsmith.com"

COPYRIGHT = ('The contents of this blog are licensed '
             '<a rel="license" '
                'href="https://creativecommons.org/licenses/by/4.0">'
             '<img title="CC-BY" '
                  'src="https://i.creativecommons.org/l/by/4.0/88x31.png" />'
             '</a>')

TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en'

THEME = 'theme/'

# Social settings {{{1
TWITTER_USERNAME = 'byronjsmith'
GITHUB_URL = 'https://github.com/bsmith89'
GITHUB_POSITION = 'right'

# Blogroll {{{2
LINKS =  [('Living in an Ivory Basement', 'http://ivory.idyll.org/blog/'),
          ('The Endeavor', 'https://www.johndcook.com/blog/'),
          ('Andrew Gelman (and others)', 'https://statmodeling.stat.columbia.edu/'),
         ]

# Social widget
SOCIAL = [('twitter', 'https://twitter.com/ByronJSmith'),
          ('linkedin', 'https://linkedin.com/profile/view?id=76273001'),
          ('github', 'https://github.com/bsmith89'),
         ]

# Template settings {{{1
DEFAULT_DATE_FORMAT= '%A, %B %-d, %Y'
MODIFIED_DATE_FORMAT = '%B %-d, %Y, %H:%M'

DEFAULT_CATEGORY = "Misc."

# Pagination settings {{{2
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 5
SUMMARY_MAX_LENGTH = 150


# Content/Organizational settings {{{1
STATIC_PATHS = ['static/',]
EXTRA_PATH_METADATA = {'static/favicon.ico': {'path': './favicon.ico'}}

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DRAFT_URL = '{slug}.html'
DRAFT_SAVE_AS = '{slug}.html'

# Extract metadata from the filename
SLUGIFY_SOURCE = 'basename'
FILENAME_METADATA = '(?P<slug>.*)'

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Development settings {{{1

# Document-relative URLs when developing.
# This must be set to False for publishing.
# See publishconf.py
RELATIVE_URLS = True

# Extras {{{1
MATHJAX = True

# Plugins {{{2
PLUGIN_PATHS = ['./plugins']
PLUGINS=[]

PLUGIN_PATHS.append('./plugins/extended_sitemap')
PLUGINS.append('extended_sitemap')
SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.6,
            'indexes': 0.5,
            'pages': 0.7,
            },
        'changefreqs': {
            'articles': 'monthly',
            'pages': 'monthly',
            'indexes': 'daily',
            },
        }

# PLUGINS.append('pandoc_reader')
# # PANDOC_FILES = ['md']
# PANDOC_FILTERS = ['pandoc-pygments-filter']
# PANDOC_ARGS = ['--preserve-tabs', '--smart']
